from django.http import HttpResponse
from django.shortcuts import render, redirect
from api.models import Login

def Logins (request) :
    if request.method == 'POST' :
        nama = str(request.POST.get('username'))
        pw = str(request.POST.get('password'))
        try:
            username = Login.objects.get(user = nama)
            request.session['username'] = username.user
            request.session['LOGIN_AUTH'] = True

            if username.password == pw :
                  return (redirect('/public'))
            else :
                  return (redirect('/login'))    
        except:
            return (redirect('/login'))        
    else :
        return (redirect('/login'))
    
def Loginso (request) :
    if request.method == 'POST' :
        nama = str(request.POST.get('username'))
        pw = str(request.POST.get('password'))
        #username = Login.objects.get(user = nama)
        password = Login.objects.get(password = '1234albi')
        request.session['username'] = password.password
        request.session['LOGIN_AUTH'] = True
        return (redirect('/public'))             
    else :
        return (redirect('/login'))



