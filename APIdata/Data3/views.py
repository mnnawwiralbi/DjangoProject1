from django.shortcuts import render

from django.http import HttpResponse

from api.models import Member2

from .delete import hapus2

from django.shortcuts import get_object_or_404, redirect


# Create your views here.

def delete (Member2) :
    return hapus2 (Member2);

def delete3 (Member2):
    queriset = Member2.objects.get(firstname = "kuyang").delete()

def delete2 (request) :
    try:
        obj = Member2.objects.get(firstname="Haku ")
        obj.delete()
        return redirect('/public/')
    except Member2.DoesNotExist:
        # Mengembalikan respons khusus jika objek tidak ditemukan
        return HttpResponse("Objek tidak ditemukan", status=404)


	


