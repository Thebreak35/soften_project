# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170925_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_ID', models.CharField(max_length=45)),
                ('First_Name', models.CharField(max_length=45)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
                ('History', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('product_Name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ID', models.CharField(max_length=45)),
                ('customer_ID', models.CharField(max_length=45)),
                ('order_Date', models.DateTimeField(verbose_name='date ordered')),
                ('payment_Detail', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={},
        ),
    ]