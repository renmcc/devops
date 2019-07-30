#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/250:09
#__author__:"ren_mcc"
from django.conf.urls import url
from views import idc_list,idc_list_v2,idc_detail_v2

urlpatterns = [
    url("^idcs/$", idc_list),
    url("^idcs/$", idc_list),
    url("^idcs_v2/$", idc_list_v2),
    url("^idcs_detail_v2/(?P<pk>[0-9]+)/$", idc_detail_v2)
]