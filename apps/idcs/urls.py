#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/250:09
#__author__:"ren_mcc"
from django.conf.urls import url
from views import idc_list,idc_list_v2,idc_detail_v2,IdcList,IdcDetail,IdcList_V4,IdcDetail_v4
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url("^idcs/$", idc_list),
    url("^idcs_v2/$", idc_list_v2, name="idc-list_v2"),
    url("^idcs_detail_v2/(?P<pk>[0-9]+)/$", idc_detail_v2, name="idc_detail_v2"),
    url("^idcs_v3/$", IdcList.as_view(), name="idc-list_v3"),
    url("^idcs_detail_v3/(?P<pk>[0-9]+)/$", IdcDetail.as_view(), name="idc_detail_v3"),
    url("^idcs_v4/$", IdcList_V4.as_view(), name="idc-list_v4"),
    url("^idcs_detail_v4/(?P<pk>[0-9]+)/$", IdcDetail_v4.as_view(), name="idc_detail_v4"),
]

urlpatterns = format_suffix_patterns(urlpatterns)