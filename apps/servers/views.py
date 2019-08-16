# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets,mixins
from servers.models import Server,NetworkDevice,IP
from servers.serializers import ServerAutoReportSerializer,NetworkDeviceSerializer,IPSerializer,ServerSerializer
from .filter import ServerFilter

# Create your views here.
class ServerAutoReportViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create：
        创建服务器记录
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer

class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定服务器信息
    list:
        返回服务器列表
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_class = ServerFilter
    filter_fields = ("hostname",)

class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定网卡信息
    list:
        返回网卡列表
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定网卡信息
    list:
        返回IP列表
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer
