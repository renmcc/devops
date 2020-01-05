# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from idcs.models import Idc

# Create your models here.
class Cabinet(models.Model):
    idc = models.ForeignKey(Idc, verbose_name="所在机房")
    name = models.CharField(max_length=255, verbose_name="机柜名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resources_cabinet"
        ordering = ["id"]




