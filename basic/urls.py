# -*- coding=utf-8 -*-
"""
-------------------------------------------------
   File Name :    urls
   Description :
   Author :       Drambo
   date :         18-1-23
-------------------------------------------------
   Change Activity:
                  18-1-23:
-------------------------------------------------
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wxService.as_view(), name='Server Service'),
]

if __name__ == '__main__':
    pass
