# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-17 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingWeb', '0029_systablecolumn_customcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systablecolumn',
            name='primarykey',
        ),
        migrations.AddField(
            model_name='systablecolumn',
            name='primarkey',
            field=models.IntegerField(db_column='PrimarKey', default=0),
        ),
    ]
