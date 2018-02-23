# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApi', '0006_auto_20171129_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('totalSale', models.PositiveIntegerField(default=0)),
                ('smsSent', models.BooleanField(default=False)),
            ],
        ),
    ]