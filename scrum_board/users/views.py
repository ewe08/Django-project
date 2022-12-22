from django.views.generic.edit import UpdateView
from django.contrib.auth import views
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserChangeForm


class ProfileView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('homepage:home')

    def get_context_data(self, **kwargs):
        context = super(
            ProfileView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Ваш профиль'
        return context


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_changed')

    def get_context_data(self, **kwargs):
        context = super(
            PasswordChangeView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Смена пароля'
        return context


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'users/password_changed.html'

    def get_context_data(self, **kwargs):
        context = super(
            PasswordChangeDoneView,
            self,
        ).get_context_data(**kwargs)
        context['title'] = 'Смена пароля'
        return context
