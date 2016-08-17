# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=60)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('confirmations', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodId', models.IntegerField(default=0)),
                ('prodName', models.CharField(max_length=60)),
                ('inStock', models.IntegerField(default=0)),
                ('reserved', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txID', models.CharField(max_length=60)),
            ],
        ),
    ]
