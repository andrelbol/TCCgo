# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fragment',
            name='line',
        ),
        migrations.AddField(
            model_name='fragment',
            name='text',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='text.Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fragment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='text',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
