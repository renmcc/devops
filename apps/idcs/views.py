# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from idcs.models import  Idc
from .serializers import IdcSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', "application/json")
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)

def idc_list(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JSONResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content, content_type="application/json")
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdcSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
            # content = JSONRenderer().render(serializer.data)
            # return HttpResponse(content, content_type="application/json")
    return HttpResponse("")

def idc_detail(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = IdcSerializer(idc)
        return JSONResponse(serializer.data)

    elif request.method == "PUT":
        content = JSONParser().PARSE(request)
        serializer = IdcSerializer(idc, data = content)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        idc.delete()
        return HttpResponse(status=204)

#############################################################版本二##############################################
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(["GET", "POST"])
def idc_list_v2(request,format=None, *args, **kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many= True)
        return Response(serializer.data)

    elif request.method == "POST":
        #使用装饰器后不需要再处理post过来的数据，可以直接序列化
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


from rest_framework.reverse import reverse
@api_view(["GET"])
def api_root(request,format=None, *args, **kwargs):
    return Response({
        "idcs": reverse("idc-list", request=request, format=format)
    })

###################################################版本三###########################################
from rest_framework.views import APIView

class IdcList(APIView):
    def get(self, request, format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定Idc信息
    list:
        返回Idc列表
    update:
        更新Idc信息
    destroy:
        删除Idc记录
    create：
        创建Idc记录
    partial_update:
        更新部分字段
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    extra_perm_map = {
        "GET": ["idcs.view_idc"]
    }












