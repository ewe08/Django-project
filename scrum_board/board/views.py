from django.views.generic import TemplateView

from .models import Task


class TasksView(TemplateView):
    """
    View class for display scrum board
    render tasks.html
    """
    template_name = 'board/board.html'

    def get_context_data(self, **kwargs):
        """
        :return: context with item
        """
        context = super().get_context_data()
        context['title'] = 'Подробнее'
        context['backlog'] = Task.objects.filter(status='Бэклог')
        context['todo'] = Task.objects.filter(status='Сделать')
        context['progress'] = Task.objects.filter(status='В процессе')
        context['test'] = Task.objects.filter(status='Тестируется')
        context['done'] = Task.objects.filter(status='Готово')

        return context
