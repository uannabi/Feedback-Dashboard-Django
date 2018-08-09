# -*- coding: utf-8 -*-

import datetime
from itertools import chain
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView

from account.forms import RegisterUserForm, LoginForm
from account.models import ProjectCounter, Resource, Projects, Clients


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('user registered')


def dashboard(request):
    '''the follwing line will retrieve the present year'''
    now = datetime.datetime.now()
    thisYear = now.year
    '''section Ends'''
    ''' below code for dashboard of capacity resource '''
    resourceCapacity = Resource.objects.all().last()  # only one entry will be here in the db so real time update
    unUtilizedResources = resourceCapacity.capacity - resourceCapacity.utilized
    '''below code I will find out ((how many projects)) ((projects Objects)) are going out right now and pass it to
       the template '''
    ongoingProject = Projects.objects.filter(isCompleted=False)
    ongoingProjectNumber = ongoingProject.count()
    '''Section Ends'''
    '''total project counter value for Q1'''
    totalInQ1 = capacityCounterQuarterWise("Q1", thisYear)
    totalInQ2 = capacityCounterQuarterWise("Q2", thisYear)
    totalInQ3 = capacityCounterQuarterWise("Q3", thisYear)
    totalInQ4 = capacityCounterQuarterWise("Q4", thisYear)
    context = {
        'thisYear': thisYear,
        'totalQ1': totalInQ1,
        'totalQ2': totalInQ2,
        'totalQ3': totalInQ3,
        'totalQ4': totalInQ4,
        'resourceCapacity': resourceCapacity,
        'unUtilizedResources': unUtilizedResources,
        'ongoingProjectNumber': ongoingProjectNumber,
        'ongoingProject': ongoingProject
    }
    return render(request, 'account/dashboard.html', context)


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')


def capacityCounterQuarterWise(quarter, thisYear):
    '''below codes for project counter object which is not completed yet'''
    projectCounter = ProjectCounter.objects.filter(year__year=thisYear, month__quarter=quarter)
    '''Section Ends'''
    totalCompletedProject = 0
    totalCompletedPhase = 0
    totalFeedbackRecieved = 0
    totalIncurruedHour = 0
    for project in projectCounter:
        totalCompletedPhase += project.total_phases_number
        totalCompletedProject += project.completed_project_number
        totalFeedbackRecieved += project.feedback_received_number
        totalIncurruedHour += project.adiva_incurred_hours
    total = {'projectCounter': projectCounter, 'totalCompletedPhase': totalCompletedPhase,
             'totalCompletedProject': totalCompletedProject,
             'totalFeedbackRecieved': totalFeedbackRecieved, 'totalIncurruedHour': totalIncurruedHour
             }
    return total
