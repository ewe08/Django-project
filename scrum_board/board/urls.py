from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('',
         views.TasksView.as_view(),
         name='tasks'
         ),
]
