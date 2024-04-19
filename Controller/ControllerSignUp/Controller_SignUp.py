from django.http import HttpResponse
from django.shortcuts import render, redirect
from api.models import Login

def SignUp (request) :
 try:
    if request.method == 'POST' :
       vervikasi = Login.objects.get(user = request.POST.get('username'))
       return (redirect('/SignUp'))
 except:
    AllDataSignUp = Login.objects.count()
    jumlah = AllDataSignUp
    
    if request.method == 'POST' :        
        isiusername = request.POST.get('username')
        userid = str(isiusername) + str(jumlah)
        password = request.POST.get('password')
        email = request.POST.get('email')
        date = request.POST.get('date')
        
        SaveDataSignUp = Login(userid=userid,user=isiusername,
        password=password,
        email=email,date=date)
        
        #simpan Object
        SaveDataSignUp.save()

        return (redirect('/login'))
    else :
        return (redirect('/SignUp'))
    



