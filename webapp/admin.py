from __future__ import unicode_literals

from django.contrib import admin

from .models import Csr

admin.site.site_header = 'Adiva Dashboard'


@admin.register(Csr)
class CsrAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':  ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

