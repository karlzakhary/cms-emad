# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import datetime
import calendar

# Create your models here.
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

class Resource(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    registered = models.DateField(default=datetime.date.today())

    def save(self, *args, **kwargs):
        subject = 'New Resource has been added'
        message = 'Resource with the name: \'{}\''.format(self.name) + " has been added to the inventory"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["karlmaged33@gmail.com", ]
        send_mail(subject, message, email_from, recipient_list,
                  fail_silently=False)
        super(Resource, self).save(*args, **kwargs)

    @property
    def remaining_time(self):
        # import pdb;pdb.set_trace()
        exp_date = add_months(self.registered,6)
        date = (exp_date - datetime.date.today())
        delta = date.days
        return delta

