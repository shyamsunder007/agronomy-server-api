# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 21:38
from __future__ import unicode_literals

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dumb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmm_id', models.CharField(max_length=20)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='farm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('house_id', models.CharField(max_length=20)),
                ('farm_area', models.CharField(max_length=20)),
                ('season_crop', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Households',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Households_lat', models.CharField(max_length=20)),
                ('Households_lon', models.CharField(max_length=20)),
                ('Households_vilid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('person_hid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='points',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farm_id', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='random',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farm_id', models.CharField(max_length=20)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='village',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='wateryield',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('well_id', models.CharField(max_length=20)),
                ('yieldd', models.CharField(max_length=20)),
                ('DateTimeField', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='well',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farm_id', models.CharField(max_length=20)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
    ]
