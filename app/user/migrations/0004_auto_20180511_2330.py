# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-11 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180511_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user_key',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='User Key'),
        ),
    ]
