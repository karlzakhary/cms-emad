# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class ResourceAdmin(admin.ModelAdmin):
    model = Resource
    list_display = ('name', 'registered','remaining_time')
    def has_add_permission(self, request):
        return True


admin.site.register(Resource, ResourceAdmin)
