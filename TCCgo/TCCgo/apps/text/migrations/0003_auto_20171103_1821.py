# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_auto_20170927_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fragment',
            name='text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='text.Text'),
        ),
    ]
