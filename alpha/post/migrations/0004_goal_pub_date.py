# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170914_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]