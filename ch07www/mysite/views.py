# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template.loader import get_template

from mysite import models

# Create your views here.

def index(request):
    products = models.Product.objects.all()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)
 
