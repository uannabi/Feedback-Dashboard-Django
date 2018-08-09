# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.views import View
from import_export import resources
# from import_export.admin import resource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from account.models import Company, Year, ProjectCounter, Months, Resource, Projects, Clients

# from core.models import ProjectCounter


admin.site.register(Company)
admin.site.register(Year)
admin.site.register(ProjectCounter)
admin.site.register(Months)
admin.site.register(Resource)
admin.site.register(Projects)
admin.site.register(Clients)


class ProjectCounter(resources.ModelResource):
    class Meta:
        model = ProjectCounter
        fields = ('id', 'month', 'year', 'company', 'completed_project_number', 'total_phases_number', 'feedback_received_number', 'adiva_incurred_hours',)
        export_order = ('id', 'month', 'year', 'company', 'completed_project_number', 'total_phases_number', 'feedback_received_number', 'adiva_incurred_hours',)


class AccountAdmin(ImportExportModelAdmin):
    resource_class = ProjectCounter
