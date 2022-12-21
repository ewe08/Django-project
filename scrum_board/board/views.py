from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Board


class BoardsView(DetailView):
    """
    View class for display scrum board
    render tasks.html
    """
    model = Board
    template_name = 'board/board.html'

    def get_object(self, queryset=None):
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
        context['title'] = 'Подробнее'
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
