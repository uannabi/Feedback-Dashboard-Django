from django.conf.urls import url, include


from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^bio/', views.bio, name = 'bio' ),
    url(r'^mindset/', views.mindset, name = 'mindset' ),
    url(r'^life/', views.life, name = 'life' ),
    url(r'^contact/', views.contact, name = 'contact'),
    url(r'^success/', views.success, name = 'success'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_details, name = 'details'),
   
    ]

