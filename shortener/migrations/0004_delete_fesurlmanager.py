# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-07 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20171206_0847'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fesURLManager',
        ),
    ]
