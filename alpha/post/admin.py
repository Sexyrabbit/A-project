# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post,Goal

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','user','pub_date')


admin.site.register(Post,PostAdmin)
admin.site.register(Goal)



