# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from serializers import UserSerializer
User = get_user_model()
# Create your views here.
class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定用户信息
    list:
        返回用户列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer





