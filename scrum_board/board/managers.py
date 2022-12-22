from django.db import models


class BoardManager(models.Manager):
    def user_boards(self, user):
        return (
            self.get_queryset().filter(
                    executors__in=[user],
                )
        )
