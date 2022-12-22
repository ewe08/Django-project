# Generated by Django 3.2.16 on 2022-12-22 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_auto_20221222_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, help_text='Исполнитель задачи.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor_tasks', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель'),
        ),
    ]
