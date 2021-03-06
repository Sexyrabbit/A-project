# -*- coding: utf-8 -*-
# the first line allow input for chinese
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,Http404

from django.template.loader import get_template

from datetime import datetime

from .models import Product

import random

# Create your views here.

def errorpage(request):
    return HttpResponse("This is error page")

def zhibo(request, tvno='0'):
    tv_list = [{'name':'Learn to love','tvcode':'643871'},
        {'name':'Love episode 1','tvcode':'625676'},
        {'name':'Fak episode 1','tvcode':'697872'},
        {'name':'Big tight ass','tvcode':'424998'},
    ]
    template = get_template('post/zhibo.html')
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())
    return HttpResponse(html)



def homepage(request, tvno='0'):
    tv_list = [{'name':'Video Example one','tvcode':'aid=8705995&page=1'},
        {'name':'Video Example two','tvcode':'aid=8705995&page=1'},]
    template = get_template('post/homepage.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())
    return HttpResponse(html)

def post_bytime(request,year,month,day,post_id='0'):
    html = "<h2>Posted on date{}/{}/{}, post id: {}</h2><hr>".format(year,month,day,int(post_id))
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



def carlist(request, maker='0'):
    car_maker = ['SAAB','Ford','Honda','Mazda','Nissan','Toyota']
    car_list = [ [],
        ['Fiesta','Focus','Modeo','EcoSport','Kuga','Mustang'],
        ['Fit','Odyssey','CR-V','City','NSX'],
        ['Mazda3','Mazda5','Mazda6','CX-3','CX-5','MX-5'],
        ['Tida','March','Livina','Sentra','Teana','X-Trail','Juke','Murano'],
        ['Camry','Altis','Yaris','86','Prius','Vios','RAV4','Wish']
    ]
    maker = int(maker)
    maker_name = car_maker[maker]
    cars = car_list[maker]
    template = get_template('post/carlist.html')
    html = template.render(locals())
    
    return HttpResponse(html)


def carprice(request, maker='0'):
    car_maker = ['Ford','Honda','Mazda']
    car_list = [[ {'model':'Fiesta','price':203500},
        {'model':'Focus','price':605000},
        {'model':'Mustang','price':900000} ],
        [ {'model':'Fit','price':450000},
        {'model':'City','price':150000},
        {'model':'NSX','price':1200000} ],
        [ {'model':'Mazda3','price':329999},
        {'model':'Mazda5','price':603000},
        {'model':'Mazda6','price':850000} ]
    ]
    maker = int(maker)
    maker_name = car_maker[maker] 
    cars = car_list[maker]
    template = get_template('post/carprice.html')
    html = template.render(locals())

    return HttpResponse(html)
