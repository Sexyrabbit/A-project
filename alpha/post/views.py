# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("hello, this is only a test")





def about(request):
    html = '''
<!DOCTYPE html>
<html>
<head><title>About this project</title></head>
<body>
<h2>A Social Network for specific ppl</h2>
<hr>
<p>
This is a test version, disclosable for internal user
</p>
</body>
</html>
'''

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
