# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post

from django.http import HttpResponse

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("NO.{}:".format(str(count)) + str(post) + "<br>")
    return HttpResponse(post_lists)

