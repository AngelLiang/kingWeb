# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-14 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingWeb', '0026_auto_20190113_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='systablelist',
            name='javascript',
            field=models.TextField(blank=True, db_column='JavaScript', null=True),
        ),
    ]
