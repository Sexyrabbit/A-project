# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

import datetime

# Create your models here.



class Post(models.Model):
    user = models.CharField(max_length=50,default="guest") # don't use constraint will reduce performance
    title = models.CharField(max_length=200)
    textbody = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    comment = models.CharField(max_length=200)

    class Meta:
        ordering = ('-pub_date',)

    #allow correct handle for chinese, this is same as __str__(self) method
    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Product(models.Model):
    SIZES = (
        ('S','Smaill'),
        ('M','Medium'),
        ('L','Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1,choices=SIZES)


class Goal(models.Model):
    TYPE = (
        ('S','Small goal'),
        ('M','Medium goal'),
        ('L','Large goal'),
        ('P','Planned goal'),
    )
    STATUS = (
        ('N','New'),
        ('I','Inprogress'),
        ('C','Completed'),
    )
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS,default='N')
    types = models.CharField(max_length=1,choices=TYPE,default='S')

    class Meta:
        ordering = ('-pub_date',)

    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return self.name




