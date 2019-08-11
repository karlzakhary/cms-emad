# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication 
from rest_framework.authentication import BasicAuthentication 

from .models import *
from .serializers import *

# disable csrf token thing
class CsrfExemptSessionAuthentication(SessionAuthentication):
  def enforce_csrf(self, request):
    return

# Create your views here.


class ResourceViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
