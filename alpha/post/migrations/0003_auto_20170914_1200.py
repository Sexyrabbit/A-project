# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={},
        ),
        migrations.RemoveField(
            model_name='goal',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='votes',
        ),
    ]