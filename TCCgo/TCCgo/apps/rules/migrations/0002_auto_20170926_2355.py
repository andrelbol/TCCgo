# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inconsistency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InconsistencyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='inconsistency',
            name='inconsistencyType_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.InconsistencyType'),
        ),
        migrations.AddField(
            model_name='inconsistency',
            name='rule_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Rule'),
        ),
    ]
