# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0019_feeduser_modified_linkedin_credentials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeduser',
            name='pref_post_repost_GPlus',
        ),
        migrations.RemoveField(
            model_name='feeduser',
            name='gplus_token',
        ),
        migrations.RemoveField(
            model_name='feeduser',
            name='gplus_token_secret',
        ),
    ]
