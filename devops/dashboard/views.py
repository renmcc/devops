# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout,authenticate
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
def meta(request):
    #请求协议
    print(request.scheme)
    #
    print(request.body)
    #请求的完整路径
    print(request.path)
    #请求方法
    print(request.method)
    print(request.encoding)
    #请求参数
    print(request.GET)
    print(request.POST)
    #客户端元数据
    print(request.META)
    #服务端主机ip
    print(request.get_host())
    print(request.get_port())
    #服务端完整路径
    print(request.get_full_path())
    print(request.is_secure())
    print(request.is_ajax())
    return HttpResponse("hello world")

def index1(request):
    data = {
        "name":"三",
        "age":18
    }
    data1 = ["a","b","c"]
    #可以传字段和列表，列表需要指定safe为False
    return JsonResponse(data1, safe=False)

#模板
from django.template import Context, loader
def index_templete(request):
    # t = loader.get_template("test.html")
    # context = {"name":"hello..."}
    # return HttpResponse(t.render(context, request))
    context = {"name": "hello..."}
    return render(request, 'test.html', context)

def index(request):
    #只读的字典，要想修改只能copy一份
    print request.GET.getlist("name")
    get_data = request.GET.copy()
    print get_data
    return HttpResponse("")

def userlogin(request):
    if request.method == "GET":
        return render(request, 'user_login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(username=username,password=password)
        if user_obj:
            login(request, user_obj)
            print "登录成功"
        else:
            print "登录失败"
            return render(request, 'user_login.html')
    return HttpResponse("")

def articles(request, *args, **kwargs):
    print args
    return HttpResponse("")

class User111():
    http_method_names = ["get","post","put","delete"]
    def as_view(self):
        def view(request, *args, **kwargs):
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.dispatch(request, *args, **kwargs)
        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handle = getattr(self, request.method.lower())
        else:
            handle = self.http_method_not_allowed
        return handle(request, *args, **kwargs)
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("")
    def get(self, request, *args, **kwargs):
        return HttpResponse("")
    def post(self, request, *args, **kwargs):
        return HttpResponse("")
    def put(self, request, *args, **kwargs):
        return HttpResponse("")
    def delete(self, request, *args, **kwargs):
        return HttpResponse("")

class MyView(View):
    def get(self, request, *args, **kwargs):
        per = 10
        try:
            page = int(request.GET.get("page",1))
        except:
            page = 1
        end = page * 10
        start = end - 10
        queryset = User.objects.all()[start:end]
        data = list(queryset.values("id","username","email"))
        return JsonResponse(data, safe=False)