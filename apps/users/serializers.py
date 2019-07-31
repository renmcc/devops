#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3110:45
#__author__:"ren_mcc"
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """
    用户序列化类
    """
    id       = serializers.IntegerField()
    username = serializers.CharField()
    email    = serializers.EmailField()
