# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0034_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='title',
            field=models.CharField(choices=[(b'FIRE', b'FIRE'), (b'LOVE', b'LOVE'), (b'CRAP', b'CRAP'), (b'OKAY', b'OKAY'), (b'BORING', b'BORING'), (b'HARD', b'HARD'), (b'TEARS', b'TEARS'), (b'INTERESTING', b'INTERESTING')], max_length=50),
        ),
    ]
