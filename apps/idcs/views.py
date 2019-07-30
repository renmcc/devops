# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from idcs.models import  Idc
from serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        kwargs.setdefault('content_type','application/json')
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)

def idc_list(request, *args, **kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JSONResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content, content_type="application/json")
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = IdcSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
    return HttpResponse("")