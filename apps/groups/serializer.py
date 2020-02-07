#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/6 17:41
#__author__ = 'ren_mcc'

from django.contrib.auth.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):

    # 序列化添加字段
    def to_representation(self, instance):
        ret = super(GroupSerializer, self).to_representation(instance)
        ret["users"] = instance.user_set.all().count()
        return ret

    class Meta:
        model = Group
        fields = ("id", "name")