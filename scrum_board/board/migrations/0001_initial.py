# Generated by Django 3.2.16 on 2022-12-14 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Текст задачи.', verbose_name='текст')),
                ('start_date', models.DateTimeField(help_text='Дата начала выполнения задачи.', verbose_name='начало')),
                ('end_date', models.DateTimeField(help_text='Дата дедлайна.', verbose_name='конец')),
                ('status', models.CharField(choices=[('Бэклог', 'Бэклог'), ('Сделать', 'Сделать'), ('В процессе', 'В процессе'), ('Тестируется', 'Тестируется'), ('Готово', 'Готово')], help_text='Состояние задачи.', max_length=20, verbose_name='состояние')),
                ('creator', models.ForeignKey(help_text='Создатель задачи.', on_delete=django.db.models.deletion.CASCADE, related_name='creator_tasks', to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
                ('executor', models.ForeignKey(help_text='Исполнитель задачи.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor_tasks', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель')),
            ],
        ),
    ]