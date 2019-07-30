#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/2610:26
#__author__:"ren_mcc"
from rest_framework import serializers
from idcs.models import Idc

class IdcSerializer(serializers.Serializer):
    """
    IDC序列化类
    """
    id          = serializers.IntegerField(read_only=True)
    name        = serializers.CharField(required=True, max_length=32)
    address     = serializers.CharField(required=True, max_length=256)
    phone       = serializers.CharField(required=True, max_length=15)
    email       = serializers.EmailField(required=True)
    letter      = serializers.CharField(required=True,max_length=5)

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.letter = validated_data.get("letter", instance.letter)
        instance.save()
        return instance
