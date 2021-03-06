# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-19 06:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('content', models.CharField(max_length=200, unique=True, verbose_name='내용')),
            ],
            options={
                'verbose_name': '칭찬',
                'verbose_name_plural': '칭찬',
            },
        ),
        migrations.CreateModel(
            name='PraiseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('choices', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='칭찬 대상 목록')),
                ('sender_key', models.CharField(max_length=200, verbose_name='보낸 사람 user key')),
                ('receiver_key', models.CharField(max_length=200, verbose_name='받은 사람 user key')),
                ('praise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='praise.Praise', verbose_name='칭찬')),
            ],
            options={
                'verbose_name': '칭찬 내역',
                'verbose_name_plural': '칭찬 내역',
            },
        ),
    ]
