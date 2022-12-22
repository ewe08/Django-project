from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path(
        '',
        views.BoardsListView.as_view(),
        name='boards',
    ),
    path(
        '<int:pk>',
        views.BoardDetailView.as_view(),
        name='tasks',
    ),
]
