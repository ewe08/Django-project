from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path(
        '<int:pk>',
        views.BoardsView.as_view(),
        name='tasks'
    ),
]
