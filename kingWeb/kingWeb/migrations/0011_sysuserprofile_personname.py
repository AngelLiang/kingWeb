# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-31 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingWeb', '0010_auto_20180830_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysuserprofile',
            name='personname',
            field=models.CharField(blank=True, db_column='PersonName', max_length=50, null=True),
        ),
    ]