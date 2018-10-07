# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.views import View
from import_export import resources
# from import_export.admin import resource
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
from account.models import Company, Year, ProjectCounter, Months, Resource, Projects,HeadsupLive

# from core.models import ProjectCounter


admin.site.register(Company)
admin.site.register(Year)
# admin.site.register(ProjectCounter)
admin.site.register(Months)
admin.site.register(Resource)


# admin.site.register(Projects)
# admin.site.register(timePeriodTesting)


class AccountAdmin(ImportExportModelAdmin):
    resource_class = ProjectCounter


# class PorjectCounterInline(admin.StackedInline):
#     model = ProjectCounter


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'projects_name', 'pDate', 'eTalents', 'budgethours', 'estimatedHours', 'runningHours', 'isCompleted')
    search_fields = ('projects_name', 'pDate',)
    list_filter = (
        ('pDate', DateRangeFilter), ('isCompleted'),
    )
    # fieldsets = [(None, {'fields': ('company', 'projects_name', 'cName', 'isCompleted',)}), ]
    # inlines = [PorjectCounterInline]


@admin.register(ProjectCounter)
class ProjectCounterAdmin(admin.ModelAdmin):
    list_display = (
        'month', 'total_phases_number', 'adiva_incurred_hours', 'feedback_received_number', 'headsup_model',)


@admin.register(HeadsupLive)
class HeadsupLiveAdmin(admin.ModelAdmin):
    list_display = (
        'start_date', 'delivery_date', 'brand_name', 'description','isLive')

    list_filter = (
        ('start_date', DateRangeFilter), ('isLive'),
    )
