# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0010_auto_20160709_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeduser',
            name='social_git',
            field=models.URLField(blank=True, default='', max_length=60, null=True),
        ),
    ]
