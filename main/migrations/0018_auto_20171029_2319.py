# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20171029_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='size',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]