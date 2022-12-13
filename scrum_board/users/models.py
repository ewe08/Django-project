from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model with additional unique email field."""
    ROLE_CHOICES = (
        ('CLIENT', 'Заказчик'),
        ('LEAD', 'Лид'),
        ('DEVELOPER', 'Разработчик'),
    )

    email = models.EmailField(
        'email',
        unique=True,
        help_text='Ваш email',
    )

    status = models.CharField(
        'Роль',
        max_length=len('DEVELOPER'),
        help_text='Ваша роль на сайте.',
        choices=ROLE_CHOICES,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
