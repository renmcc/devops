#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/250:09
#__author__:"ren_mcc"
from django.conf.urls import url
from views import idc_list

urlpatterns = [
    url("^idcs/$", idc_list)
]