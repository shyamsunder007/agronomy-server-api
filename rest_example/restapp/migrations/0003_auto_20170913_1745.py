# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-13 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20170913_1525'),
    ]

    operations = [
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
        migrations.RenameField(
            model_name='households',
            old_name='Household_id',
            new_name='Households_lon',
        ),
        migrations.RenameField(
            model_name='households',
            old_name='age',
            new_name='Households_vilid',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='farm_id',
        ),
        migrations.RemoveField(
            model_name='households',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='households',
            name='person',
        ),
        migrations.RemoveField(
            model_name='households',
            name='person_hid',
        ),
        migrations.RemoveField(
            model_name='households',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='points',
            name='points_id',
        ),
        migrations.RemoveField(
            model_name='well',
            name='well_id',
        ),
        migrations.AlterField(
            model_name='farm',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='households',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='points',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wateryield',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='well',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
