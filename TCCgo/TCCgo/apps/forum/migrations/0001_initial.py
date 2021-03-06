# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('index', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('post_id_fk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('post_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post')),
            ],
        ),
    ]
