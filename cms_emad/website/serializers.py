from rest_framework import serializers, fields
from django.conf import settings
from django.db import models
from .models import *

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('name', 'registered')
