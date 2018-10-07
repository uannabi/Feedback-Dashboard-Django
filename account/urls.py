from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from account import views
from .views import RegisterUserView, LoginUserView

urlpatterns = [
    url(r'^signup', view=RegisterUserView.as_view(), name= 'signup'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', view=views.dashboard, name='dashboard'),
    url(r'^lrwdag/$', view=views.dView, name='dView'),
    
]