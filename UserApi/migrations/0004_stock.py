# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApi', '0003_auto_20171129_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('threshold', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApi.Inventory')),
            ],
        ),
    ]
