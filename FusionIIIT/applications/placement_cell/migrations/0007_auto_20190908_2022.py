# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-08 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement_cell', '0006_auto_20190908_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conference',
            old_name='unique',
            new_name='unique_id',
        ),
        migrations.RenameField(
            model_name='extracurricular',
            old_name='unique',
            new_name='unique_id',
        ),
        migrations.RenameField(
            model_name='reference',
            old_name='unique',
            new_name='unique_id',
        ),
    ]
