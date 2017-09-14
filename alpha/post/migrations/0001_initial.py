# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('votes', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='guest', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('textbody', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('votes', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
