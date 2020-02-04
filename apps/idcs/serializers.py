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
    name        = serializers.CharField(required=True, max_length=32, label="机房名称",help_text="机房名称",
                                        error_messages={"blank":"机房名称不能为空",
                                                        "required":"这个字段为必要字段"})
    address     = serializers.CharField(required=True, max_length=256,label="机房地址",help_text="机房地址")
    phone       = serializers.CharField(required=True, max_length=15, label="机房电话",help_text="机房电话")
    email       = serializers.EmailField(required=True, label="机房邮件",help_text="机房邮件")
    letter      = serializers.CharField(required=True,max_length=5,label="机房简称",help_text="机房简称")
    #status      = serializers.BooleanField(required=True,label="机房是否启用",help_text="机房是否启用")

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.letter = validated_data.get("letter", instance.letter)
        #instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
