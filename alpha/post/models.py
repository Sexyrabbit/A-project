# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

import datetime

# Create your models here.



class Post(models.Model):
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


