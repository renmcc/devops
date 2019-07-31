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
from django.contrib import admin
from idcs.views import api_root
from rest_framework.routers import DefaultRouter
from idcs.views import IdcListViewset_V7
from users.views import UserViewset

route = DefaultRouter()
route.register("idcs", IdcListViewset_V7, base_name="idcs")
route.register("users", UserViewset, base_name="users")
urlpatterns = [
    url(r'^', include(route.urls))
]


# urlpatterns = [
#     # url(r'^admin/', admin.site.urls),
#     # url("^$", api_root),
#     # url(r'^dashboard/', include("dashboard.urls")),
#     # url(r'^idc/', include("idcs.urls")),
#     # url(r'^cmdb/', include("cmdb.urls"))
# ]

