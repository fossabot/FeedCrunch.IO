# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0020_gplus_removed'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackIntegration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('channels', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('access_token', encrypted_model_fields.fields.EncryptedCharField()),
            ],
        ),
        migrations.AddField(
            model_name='feeduser',
            name='pref_post_repost_Slack',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slackintegration',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_slack_integrations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='slackintegration',
            unique_together=set([('team_name', 'user')]),
        ),
    ]