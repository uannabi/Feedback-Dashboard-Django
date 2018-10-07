# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Csr(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='csr_post')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=100)

    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # def get_absolute_url(self):
    #     return reverse('webapp:csr_detail',
    #                    args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    objects = models.Manager()
    published = PublishedManager()
