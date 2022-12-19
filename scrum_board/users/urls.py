from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/',
         views.ProfileView.as_view(),
         name='profile'),
    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_changed',
    ),
]
