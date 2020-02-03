#!/usr/bin/env python
#coding:utf8
#__time__:2019/8/1212:01
#__author__:"ren_mcc"

import django_filters
from django.contrib.auth import get_user_model
User = get_user_model()

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']