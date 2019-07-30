# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from idcs.models import  Idc
from serializers import IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
##################################版本一###########################################
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


##################################版本二###########################################
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(["GET","POST"])
def idc_list_v2(request,*args,**kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def idc_detail_v2(request,pk, *args,**kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


from rest_framework.reverse import reverse
@api_view(["GET"])
def api_root(request, format=None, *args, **kwargs):
    return Response(
        {
            "idcs_v2":reverse("idc-list_v2", request=request,format=format),
            "idcs_v3": reverse("idc-list_v3", request=request, format=format),
           # "idc_detail_v2":reverse("idc_detail", request=request,format=format)
        }
    )


##################################版本三###########################################
from rest_framework.views import APIView
from django.http import Http404

class IdcList(APIView):
    def get(self,request, format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class IdcDetail(APIView):
    def get_object(self, pk):
        try:
            return Idc.objects.get(pk=pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, pk ,format=None):
        idc = self.get_objects(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)