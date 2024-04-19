from django.shortcuts import render

from django.http import HttpResponse

from api.models import Member2

from api.urlsfolder.urls import ApiConfigu

from django.shortcuts import get_object_or_404, redirect

from api.models import Login

# Create your views here.

def Controller (string) :
	if string == "Bahlul" :
		return "Bahlul"
	else :
		return ApiConfigu.Coba_Urls()

def my_view2 (request) :
	context = Member2.objects.all()
	namapertama = [item.firstname for item in context]
	return render (request, 'Home/index.html', {'nama' : namapertama })

def my_view3 (request) :
	context = Member2.objects.get(firstname = "Riooojaki")
	namapertama = context.lastname
	return render (request, 'Home/index.html', {'nama' : namapertama })

def my_view (request) :
    if not (request.session.get('LOGIN_AUTH') is None):  # Mengubah metode menjadi POST untuk keamanan
        username = request.session.get('username')
        password = request.session.get('password')
        # Seharusnya ada proses otentikasi di sini, misal menggunakan authenticate
        return render(request, 'Home/index.html', {'nama': username, 'belakang': password})
    else:
        # try:
        #     context = Member2.objects.get(firstname="Riooojaki")  # Asumsi hanya ada satu objek yang cocok
        #     namapertama = request.session.get('username')
        # except Member2.DoesNotExist:
        #     namapertama = "Tidak ditemukan"
        return redirect('http://127.0.0.1:8000/login/')
    
	
def Login(request):
    try:
        truedata = Login.objects.all()  # Ambil semua data dari model Login
        firstname = []
        lastname = []
        for item in truedata:  # Perbaiki variabel loop untuk sesuai dengan truedata
            firstname.append(item.firstname)
            lastname.append(item.lastname)
        Ada = "Ada"
        return render(request, 'Login/login.html', {'nama': firstname, 'belakang': lastname, 'Keterangan' : Ada})
    except :  # Mengganti Member2.DoesNotExist dengan Login.DoesNotExist jika perlu
        Ada = "TidakAda"
        firstname = "Tidak Ada"
        lastname = "Tidak Ada"
        return render(request, 'Login/login.html', {'nama': firstname, 'belakang': lastname, 'Keterangan' : Ada})

def SignUp(request):
      try:
        truedata = Login.objects.all()  # Ambil semua data dari model Login
        firstname = []
        lastname = []
        for item in truedata:  # Perbaiki variabel loop untuk sesuai dengan truedata
            firstname.append(item.firstname)
            lastname.append(item.lastname)
        Ada = "Ada"
        return render(request, 'Login/login.html', {'nama': firstname, 'belakang': lastname, 'Keterangan' : Ada})
      except:
          return render(request, 'SignUp/SignUp.html')

