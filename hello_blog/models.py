# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Note(models.Model):
    user = models.ForeignKey(auth.models.User)
    category = models.ForeignKey(Category)
    keywords = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)

    def __str__(self):
        return self.title
