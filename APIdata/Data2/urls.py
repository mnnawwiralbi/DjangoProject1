from django.urls import path, include

from django.shortcuts import render

from django.http import HttpResponse

from api.models import Member3

from rest_framework.routers import DefaultRouter

from APIdata.Data2.PostSet import add_data 

# router = DefaultRouter()
# router.register('member2', postsets)

urlpatterns = [
   path('add/api', add_data, name='add_data'),
]

# def my_view (request) :
# 	context = Member3.objects.get(namapertama = "Johan")
# 	namapertama = context.namabelakang
# 	return render (request, 'index.html', {'nama' : namapertama })

# urlpatterns = [
#     path('', my_view),
# ]
