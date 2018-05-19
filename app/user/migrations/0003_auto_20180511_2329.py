# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-11 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180508_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='youareuser',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='youareuser',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='전화번호'),
        ),
    ]