# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-24 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0019_auto_20161024_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='luggage.Invoice'),
            preserve_default=False,
        ),
    ]
