#!/usr/bin/env python
#coding:utf8
#__time__:2019/8/911:41
#__author__:"ren_mcc"

import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")

import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def get_user():
    for user in User.objects.all():
        print(user.username)

if __name__ == "__main__":
    get_user()