from django.contrib.sitemaps import Sitemap
from .models import Csr

class CsrSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Csr.published.all()

    def lasmode(self, obj):
        return obj.updated

