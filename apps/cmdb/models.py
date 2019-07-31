# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Servers(models.Model):
    server_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    server_type = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    outer_ip = models.CharField(max_length=30, blank=True, null=True)
    inner_ip = models.CharField(max_length=30, blank=True, null=True)
    enabled_flag = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=30, blank=True, null=True)
    var_file = models.CharField(max_length=255, blank=True, null=True)
    cur_operate_state = models.IntegerField(blank=True, null=True)
    cur_operate_action = models.CharField(max_length=255, blank=True, null=True)
    start_operate_time = models.DateTimeField(blank=True, null=True)
    last_operate_time = models.DateTimeField(blank=True, null=True)
    http_port = models.IntegerField(blank=True, null=True)
    shutdown_port = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servers'