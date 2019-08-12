# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from users.pagination import Pagination
from serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from filter import UserFilter
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
    #如果有不需要分页的视图可以把变量为None
    # pagination_class = Pagination

    filter_class = UserFilter
    filter_fields = ("username",)
    # authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)






