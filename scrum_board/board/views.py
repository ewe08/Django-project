from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .forms import TaskForm
from .models import Task


class TaskCreateView(FormView):
    template_name = 'board/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('homepage:home')

    def form_valid(self, form):
        Task.objects.create(
            creator=self.request.user,
            **form.cleaned_data
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Создание задачи'
        return context
