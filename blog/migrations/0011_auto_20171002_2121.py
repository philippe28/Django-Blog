# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171002_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
