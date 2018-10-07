# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_projects_updatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='budgethours',
            field=models.IntegerField(blank=True, default=True, null=True, verbose_name='Budget Hours'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='eTalents',
            field=models.IntegerField(blank=True, default=True, null=True, verbose_name='Talent Used'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='estimatedHours',
            field=models.IntegerField(blank=True, default=True, null=True, verbose_name='Estimated Hours'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='runningHours',
            field=models.IntegerField(blank=True, default=True, null=True, verbose_name='Running Hours'),
        ),
    ]