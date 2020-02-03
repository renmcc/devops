#!/usr/bin/env python
#coding:utf-8
#__time__: 2020/1/15 23:15
#__author__ = 'ren_mcc'

import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0,project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")

import django
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

def get_users():
    for user in User.objects.all():
        print(user.username)

def create_user():
    for i in range(100):
        user = 'user{0}'.format(i)
        email = 'user{0}@test.com'.format(i)
        passwd = '910202'
        User.objects.create_user(user, email, passwd)

if __name__ == "__main__":
    #get_users()
    create_user()