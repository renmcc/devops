#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3115:43
#__author__:"ren_mcc"
from rest_framework import serializers
from models import Server,NetworkDevice,IP
from manufacturer.models import Manufacturer,ProductModel


class ServerAutoReportSerializer(serializers.Serializer):
    """
    服务器同步序列化类
    """
    ip                = serializers.IPAddressField(required=True)
    hostname          = serializers.CharField(required=True,max_length=20)
    cpu               = serializers.CharField(required=True, max_length=50)
    mem               = serializers.CharField(required=True, max_length=20)
    disk              = serializers.CharField(required=True, max_length=200)
    os                = serializers.CharField(required=True, max_length=50)
    sn                = serializers.CharField(required=True, max_length=50)
    manufacturer      = serializers.CharField(required=True)
    model_name        = serializers.CharField(required=True)
    uuid              = serializers.CharField(required=True, max_length=50)
    network           = serializers.JSONField(required=True)

    def validate_manufacturer(self,value):
        try:
            return Manufacturer.objects.get(vendor_name__exact=value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)
        return value

    def create_manufacturer(self, vendor_name):
        return Manufacturer.objects.create(vendor_name=vendor_name)

    def validate(self, attrs):
        manufacturer_obj = attrs["manufacturer"]
        try:
            attrs["model_name"] = manufacturer_obj.productmodel_set.get(model_name__exact=attrs["model_name"])
        except ProductModel.DoesNotExist:
            attrs["model_name"] = self.create_product_model(attrs["model_name"], manufacturer_obj)
        print(attrs)
        return attrs

    def create_product_model(self, model_name, manufacturer_obj):
        return ProductModel.objects.create(model_name=model_name,vendor=manufacturer_obj)


    def create(self, validated_data):
        network = validated_data.pop("network")
        server_obj =  Server.objects.create(**validated_data)
        self.check_server_network_device(server_obj,network)
        return server_obj

    def check_server_network_device(self,server_obj,network):
        """
        检测指定服务器有没有这些网卡设备，并做关联
        """
        network_device_queryset = server_obj.networkdevice_set.all()
        for device in network:
            try:
                network_device_obj = network_device_queryset.get(name__exact=device["name"])
            except NetworkDevice.DoesNotExist:
                self.create_network_device(server_obj, device)

    def check_ip(self, network_device_obj, ifnets):
        ip_queryset = network_device_obj.ip_set.all()
        for ifnet in ifnets:
            try:
                ip_queryset.get(ip_addr__exact=ifnet["ip_addr"])
            except IP.DoesNotExist:
                ip_obj = self.create_ip(network_device_obj, ifnet)


    def create_ip(self, network_device_obj, ifnet):
        ifnet["device"] = network_device_obj
        return IP.objects.create(**ifnet)

    def create_network_device(self,server_obj, device):
        ips = device.pop("ips")
        device["host"] = server_obj
        network_device_obj = NetworkDevice.objects.create(**device)
        self.check_ip(network_device_obj,ips)
        return network_device_obj

class ServerSerializer(serializers.ModelSerializer):
    """
    服务器序列化类
    """
    class Meta:
        model = Server
        fields = "__all__"

class NetworkDeviceSerializer(serializers.ModelSerializer):
    """
    网卡序列化
    """
    class Meta:
        model = NetworkDevice
        fields = "__all__"

class IPSerializer(serializers.ModelSerializer):
    """
    IP序列化
    """
    class Meta:
        model = IP
        fields = "__all__"


