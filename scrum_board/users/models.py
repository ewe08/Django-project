from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model with additional unique email field."""
    email = models.EmailField(
        'email',
        unique=True,
        help_text='Ваш email',
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
