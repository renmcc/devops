#!/usr/bin/env python
#coding:utf8
#__time__:2019/8/1212:09
#__author__:"ren_mcc"

import django_filters
from .models import Server
from django.db.models import Q

class ServerFilter(django_filters.FilterSet):
    hostname = django_filters.CharFilter(method="search_hostname")

    def search_hostname(self, queryset, name, value):
        #通过Q实现多条件搜索
        return queryset.filter(Q(hostname__icontains=value)|Q(ip__icontains=value))

    class Meta:
        model = Server
        fields = ['hostname']