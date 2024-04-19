from api.models import Member2

from api.models import Member3

from django.http import HttpResponse

from django.shortcuts import render


# def hapus2 (Member2) :
#     queryset = Member2.objects.get(firstname = "Kami")
#     queryset.delete()
#     return 0


def hapus2(request):
    try:
        # Blok kode yang mungkin menghasilkan kesalahan
        queryset = Member2.objects.get(firstname = "Kami")
        queryset.delete()
        return 0
        
    except ZeroDivisionError:
        # Tangani kesalahan jika terjadi pembagian dengan nol
        return HttpResponse("Terjadi pembagian dengan nol.")
    else:
        # Blok ini akan dijalankan jika tidak ada kesalahan
        return HttpResponse("Operasi berhasil dilakukan.")
