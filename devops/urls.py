# -*- coding: utf-8 -*-
"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url,include
# from django.contrib import admin
# from rest_framework.routers import DefaultRouter
# from users.views import UserViewset,DashboardStatusViewset
# from rest_framework.documentation import include_docs_urls
# from idcs.views import IdcViewset
# from cabinet.views import CabinetViewset
# from manufacturer.views import ManufacturerViewset,ProductModelViewset
# from servers.views import  ServerAutoReportViewset,NetworkDeviceViewset,IPViewset,ServerViewset
#
# route = DefaultRouter()
# route.register("idcs", IdcViewset, base_name="idcs")
# route.register("users", UserViewset, base_name="users")
# route.register("cabinet", CabinetViewset, base_name="cabinet")
# route.register("Manufacturer", ManufacturerViewset, base_name="Manufacturer")
# route.register("ProductModel", ProductModelViewset, base_name="ProductModel")
# route.register("ServerAutoReport", ServerAutoReportViewset, base_name="ServerAutoReport")
# route.register("NetworkDevice", NetworkDeviceViewset, base_name="NetworkDevice")
# route.register("IP", IPViewset, base_name="IP")
# route.register("Server", ServerViewset, base_name="Server")
# route.register("Dashboard", DashboardStatusViewset, base_name="Dashboard")
#
# urlpatterns = [
#     url(r'^', include(route.urls)),
#     url(r'^api-auth', include("rest_framework.urls",namespace="rest_framework")),
#     url(r'^docs/', include_docs_urls("运维平台接口文档"))
# ]


# urlpatterns = [
#     # url(r'^admin/', admin.site.urls),
#     # url("^$", api_root),
#     # url(r'^dashboard/', include("dashboard.urls")),
#     # url(r'^idc/', include("idcs.urls")),
#     # url(r'^cmdb/', include("cmdb.urls"))
# ]


from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idc/', include("idcs.urls")),
]