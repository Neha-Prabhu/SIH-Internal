# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 03:16
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, max_length=255, null=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('results_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]
