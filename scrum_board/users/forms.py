from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser
from core.forms import BaseForm


class CustomUserCreationForm(UserCreationForm):
    """Custom form for creating new user."""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            CustomUser.username.field.name,
            CustomUser.email.field.name,
        )


class CustomUserChangeForm(BaseForm, UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.first_name.field.name,
            CustomUser.last_name.field.name,
        )
