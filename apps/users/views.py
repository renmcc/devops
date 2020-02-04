# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, mixins,response,permissions
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from users.pagination import Pagination
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .filter import UserFilter
from django_filters.rest_framework import DjangoFilterBackend


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
    #pagination_class = PageNumberPagination

    #自定义搜索
    filter_class = UserFilter
    filter_fields = ("username",)
    #登录认证
    #authentication_classes = (SessionAuthentication,)
    #权限认证
    # permission_classes = (IsAuthenticated,)
    #django默认get权限为空,给get加自定义权限
    # extra_perm_map = {
    #     'GET': ['auth.view_user']
    # }


class DashboardStatusViewset(viewsets.ViewSet):
    """
    list:
        返回Dashboard数据
    """
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        data = self.get_content_data()
        return response.Response(data)

    def get_content_data(self):
        return {
            "aa":11,
            "bb":22
        }


