from rest_framework import viewsets
from api.models import Member2
from .serializers import MyModelSerializer
from django.shortcuts import render
from django.http import HttpResponse

class MyModelViewSets(viewsets.ModelViewSet):
    queryset = Member2.objects.all()
    serializer_class = MyModelSerializer