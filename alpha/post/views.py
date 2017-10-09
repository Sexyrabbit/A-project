# -*- coding: utf-8 -*-
# the first line allow input for chinese
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,Http404

from django.template.loader import get_template

from .models import Product

import random

# Create your views here.

def errorpage(request):
    return HttpResponse("This is error page")

def homepage(request):
    return HttpResponse("This is test homepage")

def post_bytime(request,year,month,day,post_id):
    html = "<h2>Posted on date{}/{}/{}, post id: {}</h2><hr>".format(year,month,day,post_id)
    return HttpResponse(html)

def index(request):
    template = get_template('post/index.html')
    quotes = [ 'Jason is the king of Sun',
         'Nobody ever question that how awesome and cool Jason is',
         'Lao-zi once said, everyone should learn from Jason, yeah,jjjjj',
         'If you are poor, you should realize, money wasn\'t come from sky, money is come from bank,.', ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def about(request):
    template = get_template('post/about.html')
    quotes = [ 'Jason is the king of Sun',
        'Nobody ever question that how awesome and cool Jason is',
        'Lao-zi once said, everyone should learn from Jason, yeah,jjjjj',
        'If you are poor, you should realize, money wasn\'t come from sky, money is come from bank,.', ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def listing(request):
    products = Product.objects.all()
    template = get_template('post/list.html')
    html = template.render({'products':products})
    return HttpResponse(html)



def disp_detail(request, id_number):
    try:
        p = Product.objects.get(id=id_number)
    except Product.DoesNotExist:
        raise Http404('Didn\'t find the product')
    template = get_template('post/disp.html')
    html = template.render({'product': p})
    
    return HttpResponse(html)

