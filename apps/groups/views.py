from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import Group
from .serializer import GroupSerializer
from .filter import GroupFilter

class GroupsViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    filter_class = GroupFilter
    filter_field = ("name",)