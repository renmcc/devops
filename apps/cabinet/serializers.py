#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3113:48
#__author__:"ren_mcc"
from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    #外键,主键关联的类型，一对一，一对多，多对多，都用这个类型
    #many=False意思是关联是一对多还是多对多
    idc = serializers.PrimaryKeyRelatedField(many=False,queryset=Idc.objects.all(),help_text="所在机房")
    name = serializers.CharField(required=True,max_length=255,help_text="机柜名称")

    #这个方法是序列化转json的最后一部，可以在里面修改数据
    def to_representation(self, instance):
        """
        序列化转json前的最后一步
        :param instance:
        :return:
        """
        idc_obj = instance.idc
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret["idc"] = {
            "id": idc_obj.id,
            "name":idc_obj.name
        }
        return ret

    def to_internal_value(self, data):
        """
        反序列化第一步：拿到提交过来的原始数据：QueryDict => request.GET request.POST
        """
        #print(data)
        return super(CabinetSerializer,self).to_internal_value(data)

    def create(self, validated_data):
        #raise serializers.ValidationError("create error")
        return Cabinet.objects.create(**validated_data)