# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preaching',
            old_name='audiofile',
            new_name='audio_file',
        ),
        migrations.RemoveField(
            model_name='series',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='series',
            name='duration',
        ),
        migrations.AddField(
            model_name='preaching',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='preaching',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='series',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
