from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Board, Task


class BoardsListView(generic.ListView):
    """
    List of all boards for a specific user
    render
    """
    model = Board
    template_name = 'board/list.html'

    def get_context_data(self):
        context = super().get_context_data()
        user = self.request.user
        context['title'] = 'Доски'
        context['boards'] = Board.objects.user_boards(user)
        return context


class BoardDetailView(generic.DetailView):
    """
    View class for display scrum board
    render board/board.html
    """
    model = Board
    template_name = 'board/board.html'

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
        print(board.pk)
        context['title'] = 'Подробнее'
        context['board'] = board.pk
        context['backlog'] = board.tasks.filter(
            status='Бэклог'
        )
        context['todo'] = board.tasks.filter(
            status='Сделать'
        )
        context['progress'] = board.tasks.filter(
            status='В процессе'
        )
        context['test'] = board.tasks.filter(
            status='Тестируется'
        )
        context['done'] = board.tasks.filter(
            status='Готово'
        )
        return context


class TaskCreateView(generic.FormView):
    """Form for creating a task"""
    template_name = 'board/create_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = Task.objects.create(
            creator=self.request.user,
            **form.cleaned_data
        )
        Board.objects.get(pk=self.kwargs['pk']).tasks.add(task)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('board:tasks', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Создание задачи'
        return context
