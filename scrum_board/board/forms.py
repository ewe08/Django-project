from django import forms

from .models import Task, Board
from core.forms import BaseForm


class TaskForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Task
        exclude = (
            Task.creator.field.name,
        )


class BoardCreateForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Board
        exclude = (
            Board.name,
        )
        fields = ['name', 'executors']
