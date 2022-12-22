from django.db import models

from .managers import BoardManager
from users.models import CustomUser


class Task(models.Model):
    """
    The task that the user has set. Has a executor, creator,
    text, timeline and status.
    """

    STATUS_CHOICES = (
        ('Бэклог', 'Бэклог'),
        ('Сделать', 'Сделать'),
        ('В процессе', 'В процессе'),
        ('Тестируется', 'Тестируется'),
        ('Готово', 'Готово'),
    )
    creator = models.ForeignKey(
        CustomUser,
        verbose_name='создатель',
        on_delete=models.CASCADE,
        help_text='Создатель задачи.',
        related_name='creator_tasks',
    )

    executor = models.ForeignKey(
        CustomUser,
        verbose_name='исполнитель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Исполнитель задачи.',
        related_name='executor_tasks',
    )

    text = models.TextField(
        verbose_name='текст',
        help_text='Текст задачи.',
    )

    start_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='начало',
        help_text='Дата начала выполнения задачи.',
    )

    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='конец',
        help_text='Дата дедлайна.',
    )

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=20,
        verbose_name='состояние',
        help_text='Состояние задачи.',
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.text


class Board(models.Model):
    """
    A board where tasks of several users are stored
    """
    objects = BoardManager()
    name = models.CharField(
        max_length=30,
        verbose_name='название',
        help_text='Название доски.',
    )

    executors = models.ManyToManyField(
        CustomUser,
        verbose_name='исполнители',
        help_text='Участники доски.',
    )

    class Meta:
        verbose_name = 'доска'
        verbose_name_plural = 'доски'

    def __str__(self):
        return f'Доска {self.name} #{self.pk}'
