# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-15 23:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0017_auto_20170518_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='_semester',
        ),
    ]