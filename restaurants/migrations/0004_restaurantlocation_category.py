# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-04 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20171204_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
