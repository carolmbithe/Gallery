# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20181102_1636'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
