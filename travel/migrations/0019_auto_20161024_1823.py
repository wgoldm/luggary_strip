# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-24 15:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luggage', '0018_auto_20161021_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default=b'', max_length=64)),
                ('amount', models.FloatField()),
                ('comments', models.TextField()),
                ('invoice_date', models.DateTimeField()),
                ('invoice_due_date', models.DateTimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
    ]
