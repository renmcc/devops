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

    #1、验证传进来的制造商是否存在，不存在创建，最终返回制造商实例
    def validate_manufacturer(self,value):
        try:
            return Manufacturer.objects.get(vendor_name__exact=value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)

    #1.1、创建制造商
    def create_manufacturer(self, vendor_name):
        return Manufacturer.objects.create(vendor_name=vendor_name)

    #2、验证制造商型号是否存在，只能在对象级别验证，不存在创建，最终返回制造商型号实例
    def validate(self, attrs):
        manufacturer_obj = attrs["manufacturer"]
        try:
            attrs["model_name"] = manufacturer_obj.productmodel_set.get(model_name__exact=attrs["model_name"])
        except ProductModel.DoesNotExist:
            attrs["model_name"] = self.create_product_model(attrs["model_name"], manufacturer_obj)
        return attrs

    #2.1、创建制造商型号
    def create_product_model(self, model_name, manufacturer_obj):
        return ProductModel.objects.create(model_name=model_name,vendor=manufacturer_obj)

    #3.1、创建提交数据
    def create_server(self, validated_data):
        print 'create'
        #server model没有这个字段，所以先拿出来
        network = validated_data.pop("network")
        #创建对象，返回server的实例
        server_obj =  Server.objects.create(**validated_data)
        #检测网卡，没有创建
        self.check_server_network_device(server_obj,network)
        return server_obj


    #3、post提交走create方法
    def create(self, validated_data):
        uuid = validated_data['uuid'].lower()
        sn   = validated_data['sn'].lower()
        try:
            if uuid == sn or sn.startswitch("vmware"):
                #虚拟机
                server_obj = Server.objects.get(uuid__icontains=uuid)
            else:
                #物理机
                server_obj = Server.objects.get(sn__icontains=sn)
        except Server.DoesNotExist:
            return self.create_server(validated_data)
        else:
            return self.update_server(server_obj, validated_data)

    def update_server(self, instance, validated_data):
        print 'update'
        instance.hostname = validated_data.get("hostname", instance.hostname)
        instance.cpu = validated_data.get("cpu", instance.cpu)
        instance.mem = validated_data.get("mem", instance.mem)
        instance.disk = validated_data.get("disk", instance.disk)
        instance.os = validated_data.get("os", instance.os)
        instance.save()
        self.check_server_network_device(instance, validated_data["network"])
        return instance

    #3.1、检测服务器有没有给过来的网卡，没有创建，最终返回实例
    def check_server_network_device(self,server_obj,network):
        """
        检测指定服务器有没有这些网卡设备，并做关联
        """
        network_device_queryset = server_obj.networkdevice_set.all()
        current_network_device_queryset = []
        for device in network:
            try:
                network_device_obj = network_device_queryset.get(name__exact=device["name"])
            except NetworkDevice.DoesNotExist:
                network_device_obj = self.create_network_device(server_obj, device)
            self.check_ip(network_device_obj, device["ips"])
            current_network_device_queryset.append(network_device_obj)

        for network_device_obj in set(network_device_queryset) - set(current_network_device_queryset):
            network_device_obj.delete()

    #3.2、创建网卡，并返回实例
    def create_network_device(self,server_obj, device):
        ips = device.pop("ips")
        #host是外键，需要server实例
        device["host"] = server_obj
        #获取network实例
        network_device_obj = NetworkDevice.objects.create(**device)
        return network_device_obj
    #3.3、检测网卡ip，不存在创建
    def check_ip(self, network_device_obj, ifnets):
        ip_queryset = network_device_obj.ip_set.all()
        current_ip_queryset = []
        for ifnet in ifnets:
            try:
                ip_obj = ip_queryset.get(ip_addr__exact=ifnet["ip_addr"])
            except IP.DoesNotExist:
                ip_obj = self.create_ip(network_device_obj, ifnet)
            current_ip_queryset.append(ip_obj)
        #去除
        for ip_obj in set(ip_queryset) - set(current_ip_queryset):
            ip_obj.delete()

    #3.4、创建网卡ip
    def create_ip(self, network_device_obj, ifnet):
        ifnet["device"] = network_device_obj
        return IP.objects.create(**ifnet)

    #4、返回的json
    def to_representation(self, instance):
        ret = {
            "hostname":instance.hostname,
            "ip": instance.ip,
            "aaa":"bbb"
        }
        return ret



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


