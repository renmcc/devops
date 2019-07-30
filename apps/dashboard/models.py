# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class Idc(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    letter = models.CharField(max_length=5)
    class Meta:
        pass

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField("中文名字",max_length=20)
    user = models.OneToOneField(User)