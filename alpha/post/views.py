# -*- coding: utf-8 -*-
# the first line allow input for chinese
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,Http404

from django.template.loader import get_template

from .models import Product

import random

# Create your views here.

def index(request):
    return HttpResponse("hello, this is only a test")


def about(request):
    template = get_template('post/about.html')
    quotes = [ 'Some pressure is given by yourself and you can use it to be extra time effective',
        'Remember to Gamelize your project',
        'Live as if it\'s a game',
        'You are empowering yourself', ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def listing(request):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>Product list</title>
</head>
<body>
<h2>Below list the training classes available for select</h2>
<hr>
<table width=400 border=1 bgcolor='%ccffcc'>
{}
</table>
</body>
</html>
'''
    products = Product.objects.all()
    tags = '<tr><td>Class Name</td><td>Price</td><td>Available class</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.sku)
    return HttpResponse(html.format(tags))




def disp_detail(request, id_number):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>{}</title>
</head>
<body>
<h2>{}</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
<a href='/post/list'>Return</a>
</body>
</html>
'''
    try:
        p = Product.objects.get(id=id_number)
    except Product.DoesNotExist:
        raise Http404('Didn\'t find the product')
    tags = '<tr><td>Product id</td><td>{}</td></tr>'.format(p.id)
    tags = tags + '<tr><td>Product name</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>Product price</td><td>{}</td></tr>'.format(p.price)
    tags = tags + '<tr><td>Available number</td><td>{}</td></tr>'.format(p.sku)
    return HttpResponse(html.format(p.name,p.name,tags))

