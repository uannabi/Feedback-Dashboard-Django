
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^ag-admin/', admin.site.urls),
    url(r'^', include('webapp.urls')),
    url(r'^account/', include('account.urls')),
]

urlpatterns += staticfiles_urlpatterns()
