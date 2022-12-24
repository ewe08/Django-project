from django.db import models


class BoardManager(models.Manager):
    def user_boards(self, user):
        return (
                self.get_queryset().filter(creator=user,) |
                self.get_queryset().filter(executors__in=[user])
        )


class TaskManager(models.Manager):
    def next(self):
        if self.status == 'Бэклог':
            self.status = 'Сделать'
        return self
