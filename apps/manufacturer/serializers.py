#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3115:43
#__author__:"ren_mcc"
from rest_framework import serializers
from models import Manufacturer,ProductModel


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

    #字段级别验证  validate_字段名
    # def validate_model_name(self,vale):
    #     return vale

    #对整个表所有字段进行操作,判断提交数据数据库中是否存在
    def validate(self,attrs):
        manufacturer_obj = attrs["vendor"]
        try:
            manufacturer_obj.productmodel_set.filter(model_name__exact=attrs["model_name"])
            raise serializers.ValidationError("该型号已经存在")
        except ProductModel.DoesNotExist:
            return attrs

    def to_representation(self, instance):
        vendor = instance.vendor
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret["vendor"]= {
            "id":vendor.id,
            "name":vendor.vendor_name
        }
        return ret