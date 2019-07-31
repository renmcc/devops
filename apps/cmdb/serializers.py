#!/usr/bin/env python
#coding:utf8
#__time__:2019/7/3018:26
#__author__:"ren_mcc"
from rest_framework import serializers
from cmdb.models import Servers

class ServersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    server_id = serializers.IntegerField()
    area_id = serializers.IntegerField()
    server_type = serializers.CharField(max_length=11)
    name = serializers.CharField(max_length=30)
    outer_ip = serializers.CharField(max_length=30)
    inner_ip = serializers.CharField(max_length=30)
    enabled_flag = serializers.IntegerField()
    group_name = serializers.CharField(max_length=30)
    var_file = serializers.CharField(max_length=255)
    cur_operate_state = serializers.IntegerField()
    cur_operate_action = serializers.CharField(max_length=255)
    start_operate_time = serializers.DateTimeField()
    last_operate_time = serializers.DateTimeField()
    http_port = serializers.IntegerField()
    shutdown_port = serializers.IntegerField()
    note = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Servers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.server_id = validated_data.get("server_id", instance.server_id)
        instance.area_id = validated_data.get("area_id", instance.area_id)
        instance.server_type = validated_data.get("server_type", instance.server_type)
        instance.name = validated_data.get("name", instance.name)
        instance.outer_ip = validated_data.get("outer_ip", instance.outer_ip)
        instance.inner_ip = validated_data.get("inner_ip", instance.inner_ip)
        instance.enabled_flag = validated_data.get("enabled_flag", instance.enabled_flag)
        instance.group_name = validated_data.get("group_name", instance.group_name)
        instance.var_file = validated_data.get("var_file", instance.var_file)
        instance.cur_operate_state = validated_data.get("cur_operate_state", instance.cur_operate_state)
        instance.cur_operate_action = validated_data.get("cur_operate_action", instance.cur_operate_action)
        instance.start_operate_time = validated_data.get("start_operate_time", instance.start_operate_time)
        instance.last_operate_time = validated_data.get("last_operate_time", instance.last_operate_time)
        instance.http_port = validated_data.get("http_port", instance.http_port)
        instance.shutdown_port = validated_data.get("shutdown_port", instance.shutdown_port)
        instance.note = validated_data.get("note", instance.note)
        instance.save()
        return instance