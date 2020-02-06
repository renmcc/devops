#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/2/6 17:41
#__author__ = 'ren_mcc'

from django.contrib.auth.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ("id", "name")