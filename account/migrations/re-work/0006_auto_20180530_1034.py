# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180530_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_project_number', models.IntegerField(verbose_name='Completed Porject Number')),
                ('total_phases_number', models.IntegerField(verbose_name='Total Phase Number')),
                ('feedback_received_number', models.IntegerField(verbose_name='Feedback Received Number')),
                ('adiva_incurred_hours', models.TimeField(default=0, verbose_name='Adiva Incurred Hours')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='company_representative_designation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Representative Designation'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_mail',
            field=models.CharField(blank=True, max_length=100, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_region',
            field=models.CharField(blank=True, max_length=25, verbose_name='Company Location'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_representative',
            field=models.CharField(blank=True, max_length=150, verbose_name='Company Representative'),
        ),
        migrations.AddField(
            model_name='projectcounter',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Company', verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='projectcounter',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Months'),
        ),
        migrations.AddField(
            model_name='projectcounter',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Year'),
        ),
    ]