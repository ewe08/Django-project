from django import forms

from .models import Task
from core.forms import BaseForm


class TaskForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Task
        exclude = (
            Task.creator.field.name,
        )
