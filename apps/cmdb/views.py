# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from cmdb.models import Servers
from cmdb.serializers import ServersSerializer
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class ServersListViewset(viewsets.ModelViewSet):
    queryset = Servers.objects.all()
    serializer_class = ServersSerializer
