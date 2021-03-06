# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20180704_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcounter',
            options={'verbose_name_plural': 'Monthly'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Daily'},
        ),
        migrations.AddField(
            model_name='projects',
            name='cName',
            field=models.CharField(default='Enter Contact Person Name', max_length=250, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_name',
            field=models.CharField(default='Enter Project Name', max_length=250, verbose_name=' Project Name'),
        ),
    ]
