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
        '<int:pk>/',
        views.BoardDetailView.as_view(),
        name='tasks',
    ),

    path(
        '<int:pk>/create_task/',
        views.TaskCreateView.as_view(
            extra_context={'title': 'Создание задачи'}
        ),
        name='create_task'
    ),
    path(
        'create_board/',
        views.BoardCreateView.as_view(),
        name='create_board'
    ),
    path(
        '<int:board_id>/<int:task_id>/next',
        views.next,
        name='next_state',
    ),
    path(
        '<int:board_id>/<int:task_id>/last',
        views.last,
        name='last_state',
    )

]
