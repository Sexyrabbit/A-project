# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about),
    url(r'^list/$',views.listing),
    url(r'^list/([0-9a-zA-Z]+)/$',views.disp_detail),
    url(r'^(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})(?P<post_id>\d{2})$',views.post_bytime),
]
