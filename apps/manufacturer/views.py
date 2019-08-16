# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from manufacturer.models import Manufacturer,ProductModel
from manufacturer.serializers import ManufacturerSerializer,ProductModelSerializer

# Create your views here.
class ManufacturerViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定制造商信息
    list:
        返回制造商列表
    update:
        更新制造商信息
    destroy:
        删除制造商记录
    create：
        创建制造商记录
    partial_update:
        更新制造商部分字段
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer



class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定型号信息
    list:
        返回型号列表
    update:
        更新型号信息
    destroy:
        删除型号记录
    create：
        创建型号记录
    partial_update:
        更新型号部分字段
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer