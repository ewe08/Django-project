from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('create_task/',
         views.TaskCreateView.as_view(),
         name='create_task'),
]
