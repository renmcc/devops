#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/1/15 23:15
#__author__ = 'ren_mcc'

import sys
import os
import django

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0,project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")

django.setup()

from django.contrib.auth.models import User
def get_users():
    for user in User.objects.all():
        print(user.username)

if __name__ == "__main__":
    get_users()