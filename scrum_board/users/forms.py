from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser
from core.forms import BaseForm


class CustomUserChangeForm(BaseForm, UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.first_name.field.name,
            CustomUser.last_name.field.name,
        )
