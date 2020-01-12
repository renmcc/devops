#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3115:43
#__author__:"ren_mcc"
from rest_framework import serializers
from .models import Manufacturer,ProductModel

#ModelSerializer用于简单的模型序列化，简单，create和update方法不用再创建
class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"

#型号序列化
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

    #反序列化自定义字段,以validate_开头
    #加需要修改的字段名字，这里以model_name为例子
    def validate_model_name(self,vale):
        return vale

    #反序列化对整个表所有字段进行验证操作,判断提交数据数据库中是否存在
    def validate(self,attrs):
        manufacturer_obj = attrs["vendor"]
        try:
            manufacturer_obj.productmodel_set.get(model_name__exact=attrs["model_name"])
            raise serializers.ValidationError("该型号已经存在")
        except ProductModel.DoesNotExist:
            return attrs

    #转json最后一步，修改返回前端的数据
    def to_representation(self, instance):
        #默认返回主键id，再添加一个name字段
        vendor = instance.vendor
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret["vendor"]= {
            "id":vendor.id,
            "name":vendor.vendor_name
        }
        return ret