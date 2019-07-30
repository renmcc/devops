#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/2610:26
#__author__:"ren_mcc"
from rest_framework import serializers

class IdcSerializer(serializers.Serializer):
    """
    IDC序列化类
    """
    id          = serializers.IntegerField()
    name        = serializers.CharField()
    address     = serializers.CharField()
    phone       = serializers.CharField()
    email       = serializers.EmailField()
    letter      = serializers.CharField()