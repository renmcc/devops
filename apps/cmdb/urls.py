#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3018:24
#__author__:"ren_mcc"
from rest_framework.routers import DefaultRouter
from cmdb.views import ServersListViewset
from django.conf.urls import url,include

route = DefaultRouter()
route.register("servers", ServersListViewset)
urlpatterns = [
    url(r'^', include(route.urls))
]