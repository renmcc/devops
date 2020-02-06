#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/6 17:50
#__author__ = 'ren_mcc'

from rest_framework.routers import DefaultRouter
from .views import GroupsViewset

group_router = DefaultRouter()
group_router.register(r'Groups', GroupsViewset, base_name='Groups')