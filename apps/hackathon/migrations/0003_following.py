# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 23:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_auto_20170629_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='hackathon.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='hackathon.User')),
            ],
        ),
    ]
