# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    registered = models.DateField(auto_now=True)
