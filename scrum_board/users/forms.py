from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.first_name.field.name,
            CustomUser.last_name.field.name,
        )
