# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-02 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
        ('applications', '0021_new_applications_20200402_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='application',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='applications.HackerApplication'),
        ),
    ]
