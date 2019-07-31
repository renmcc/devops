# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from idcs.models import  Idc
from serializers import IdcSerializer
from rest_framework import viewsets


# Create your views here.
class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定Idc信息
    list:
        返回Idc列表
    update:
        更新Idc信息
    destroy:
        删除Idc记录
    create：
        创建Idc记录
    partial_update:
        更新部分字段
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer












