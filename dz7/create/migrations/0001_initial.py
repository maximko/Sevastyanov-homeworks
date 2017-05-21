# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 10:43
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='Почта:')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон:')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Возраст:')),
                ('region', models.CharField(blank=True, max_length=20, null=True, verbose_name='Регион:')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='Имя которое не нужно:')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roadmap_name', models.CharField(max_length=50, verbose_name='Название Roadmap:')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название задачи:')),
                ('state', models.BooleanField(verbose_name='Задача решена?')),
                ('estimate', models.DateTimeField(verbose_name='Срок выполнения:')),
                ('creation_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='scores', serialize=False, to='create.Task')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата зачисления очков:')),
                ('points', models.DecimalField(decimal_places=3, max_digits=6, null=True, verbose_name='Зачислено очков:')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='roadmap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create.Roadmap'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
