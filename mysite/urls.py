from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from webapp.sitemaps import CsrSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemap = {
    'csrs': CsrSitemap,
}

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^ag-admin/', admin.site.urls),
    url(r'^', include('webapp.urls')),
    url(r'^account/', include('account.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'account.views.not_found'
handler500 = 'account.views.server_error'
handler403 = 'account.views.permission_denied'
handler400 = 'account.views.bad_request'
