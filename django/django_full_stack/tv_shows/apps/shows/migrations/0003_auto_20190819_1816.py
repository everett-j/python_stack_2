# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-19 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20190819_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.DecimalField(decimal_places=2, default=19.99, max_digits=999),
        ),
    ]