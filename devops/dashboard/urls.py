#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/1720:27
#__author__:"ren_mcc"
from django.conf.urls import url,include
from django.contrib import admin
from .views import index, index_templete, userlogin, articles, User, MyView

urlpatterns = [
    url(r'^hello/', index, name='index'),
    url(r'^hellot/', index_templete, name='index_templete'),
    url(r'^userlogin/', userlogin, name='userlogin'),
    url(r'^articles/([0-9]{4})/$', articles, name="articles"),
    #url(r'^users/', User.as_view())
    url(r'^myview/', MyView.as_view())
]