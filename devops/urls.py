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
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from idcs.views import IdcViewset
from users.views import UserViewset, DashboardStatusViewset
from cabinet.views import CabinetViewset
from manufacturer.views import ManufacturerViewset,ProductModelViewset
from servers.views import ServerAutoReportViewset,ServerViewset,NetworkDeviceViewset,IPViewset

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPICodec
schema_view = get_schema_view(title='API', renderer_classes=[SwaggerUIRenderer, OpenAPICodec])
from rest_framework_jwt.views import obtain_jwt_token


route = DefaultRouter()

route.register("idcs", IdcViewset, base_name="idcs")
route.register("users",UserViewset , base_name="users")
route.register("DashboardStatus",DashboardStatusViewset , base_name="DashboardStatus")
route.register("cabinet",CabinetViewset , base_name="cabinet")
route.register("Manufacturer",ManufacturerViewset , base_name="Manufacturer")
route.register("ProductModel",ProductModelViewset , base_name="ProductModel")
route.register("ServerAutoReport",ServerAutoReportViewset , base_name="ServerAutoReport")
route.register("Server",ServerViewset , base_name="Server")
route.register("NetworkDevice",NetworkDeviceViewset , base_name="NetworkDevice")
route.register("IP",IPViewset , base_name="IP")

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^api-auth', include("rest_framework.urls")),
    url(r'^docs/', include_docs_urls("运维接口文档")),
    #url(r'docs/', schema_view, name='运维接口文档'),
    url(r'^api-token-auth/', obtain_jwt_token),
]

# from rest_framework.authtoken import views
# urlpatterns += [
#     url(r'^api-token-auth/', views.obtain_auth_token)
# ]