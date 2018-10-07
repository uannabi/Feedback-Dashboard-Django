# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Months(models.Model):
    month = models.CharField(max_length=25)
    quarter = models.CharField(max_length=10)

    def __str__(self):
        return str(self.month)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Company(models.Model):
    company_name = models.CharField("Company Name", max_length=100)
    company_representative = models.CharField("Company Representative", max_length=150, blank=True)
    company_region = models.CharField("Company Location", max_length=25, blank=True)
    company_mail = models.CharField("Company Name", max_length=100, blank=True)
    company_representative_designation = models.CharField(max_length=100, verbose_name="Representative Designation",
                                                          blank=True)

    def __str__(self):
        return str(self.company_name) + ' ' + str(self.company_mail) + ' ' + str(self.company_region) + ' ' + str(
            self.company_representative)


class ProjectCounter(models.Model):
    month = models.ForeignKey(Months, verbose_name="Month", on_delete=models.CASCADE)
    year = models.ForeignKey(Year, verbose_name="Year", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Company Name", on_delete=models.CASCADE)
    completed_project_number = models.IntegerField("Completed Porject Number", null=True, blank=True)
    total_phases_number = models.IntegerField("Total Phase Number", null=True, blank=True)
    feedback_received_number = models.IntegerField("Feedback Received Number", null=True, blank=True)
    adiva_incurred_hours = models.IntegerField("Incurred Hours", null=True, blank=True)
    headsup_model = models.IntegerField("Heads Up", null=True, blank=True)

    def __str__(self):
        return "Client : " + str(self.company) + '\nHistory of :' + str(
            self.month)

    class Meta:
        verbose_name_plural = "Monthly"


class Resource(models.Model):
    company = models.ForeignKey(Company, verbose_name="Company Name", on_delete=models.CASCADE)
    capacity = models.IntegerField("Resource Capacity")
    utilized = models.IntegerField("Resource Utilized")

    def __str__(self):
        return "Company Name:" + str(self.company) + '\nNumber of Project Utilized ' + str(self.utilized)


class Projects(models.Model):
    company = models.ForeignKey(Company, verbose_name="Client Name", on_delete=models.CASCADE)
    projects_name = models.CharField(" Brand Name", max_length=250, default='Enter Project Name')
    pDate = models.DateField("initiation date", null=True, blank=True)
    eTalents = models.IntegerField("Talent Used", default=True,null=True, blank=True)
    budgethours = models.IntegerField("Budget Hours", default=True,null=True, blank=True)
    estimatedHours = models.IntegerField("Estimated Hours", default=True,null=True, blank=True)
    runningHours = models.IntegerField("Running Hours", default=True,null=True, blank=True)
    isCompleted = models.BooleanField(default=False, verbose_name="Completed")
    updatedTime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Daily"

    def __str__(self):
        return "Project : " + str(self.projects_name)


class HeadsupLive(models.Model):
    start_date = models.DateField("ETA", null=True, blank=True)
    delivery_date = models.DateField("ETD", null=True, blank=True)
    brand_name = models.CharField("Brand/Project", max_length=100, null=True, blank=True)
    scope_of_work = models.CharField("Scope of Work", max_length=250, blank=True, null=True)
    description = models.CharField("Additional Information", max_length=500, null=True, blank=True)
    isLive = models.BooleanField(default=False, verbose_name="Live")

    def __str__(self):
        return "Heads up for :" + str(self.brand_name)
