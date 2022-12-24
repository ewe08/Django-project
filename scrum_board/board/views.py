from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, BoardCreateForm
from .models import Board, Task


class BoardsListView(UserPassesTestMixin, generic.ListView):
    """
    List of all boards for a specific user
    render
    """
    model = Board
    template_name = 'board/list.html'

    def test_func(self):
        return (self.request.user.is_authenticated
                and self.request.user.is_active)

    login_url = reverse_lazy('users:login')

    def get_context_data(self):
        context = super().get_context_data()

        user = self.request.user
        context['title'] = 'Доски'
        context['boards'] = Board.objects.user_boards(user)
        return context


class BoardDetailView(UserPassesTestMixin, generic.DetailView):
    """
    View class for display scrum board
    render board/board.html
    """
    model = Board
    template_name = 'board/board.html'

    def test_func(self):
        return (self.request.user.is_authenticated
                and self.request.user.is_active)

    login_url = reverse_lazy('users:login')

    def get_object(self):
        return get_object_or_404(
            Board,
            pk=self.kwargs['pk'],
        )

    def get_context_data(self, **kwargs):
        """
        :return: context with item
        """
        context = super().get_context_data()
        board = self.get_object()
        context['board'] = board.pk
        context['title'] = 'Подробнее'
        context['board'] = board.pk
        tasks = board.tasks.all()
        context['backlog'] = tasks.filter(
            status='Бэклог'
        )
        context['todo'] = tasks.filter(
            status='Сделать'
        )
        context['progress'] = tasks.filter(
            status='В процессе'
        )
        context['test'] = tasks.filter(
            status='Тестируется'
        )
        context['done'] = tasks.filter(
            status='Готово'
        )
        return context


class TaskCreateView(UserPassesTestMixin, generic.FormView):
    """Form for creating a task"""
    template_name = 'board/create_task.html'
    form_class = TaskForm

    def test_func(self):
        return (self.request.user.is_authenticated
                and self.request.user.is_active)

    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        task = Task.objects.create(
            creator=self.request.user,
            **form.cleaned_data
        )
        Board.objects.get(pk=self.kwargs['pk']).tasks.add(task)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('board:tasks', kwargs={'pk': self.kwargs['pk']})


class BoardCreateView(UserPassesTestMixin, generic.FormView):
    """Form for creating Board"""
    template_name = 'board/create_board.html'
    form_class = BoardCreateForm
    success_url = reverse_lazy('homepage:home')

    def test_func(self):
        return (self.request.user.is_authenticated
                and self.request.user.is_active)

    login_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        """
        :return: context with title
        """
        context = super().get_context_data()
        context['title'] = 'Создание доски'
        return context

    def form_valid(self, form):
        board = form.save(commit=False)
        board.creator = self.request.user
        board.save()
        form.save_m2m()
        return super(BoardCreateView, self).form_valid(form)


def next(requests, board_id, task_id):
    item = Task.objects.get(pk=task_id)
    if item.status == 'Бэклог':
        item.status = 'Сделать'
    elif item.status == 'Сделать':
        item.status = 'В процессе'
    elif item.status == 'В процессе':
        item.status = 'Тестируется'
    elif item.status == 'Тестируется':
        item.status = 'Готово'
    item.save()
    return redirect('board:tasks', pk=board_id)


def last(requests, board_id, task_id):
    item = Task.objects.get(pk=task_id)
    if item.status == 'Готово':
        item.status = 'Тестируется'
    elif item.status == 'Тестируется':
        item.status = 'В процессе'
    elif item.status == 'В процессе':
        item.status = 'Сделать'
    elif item.status == 'Сделать':
        item.status = 'Бэклог'
    item.save()
    return redirect('board:tasks', pk=board_id)
