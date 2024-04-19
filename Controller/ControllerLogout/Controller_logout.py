from django.http import HttpResponse
from django.shortcuts import render, redirect


def logout (request):
    request.session['LOGIN_AUTH'] = True
    del request.session['LOGIN_AUTH']
    return (redirect('/login'))
    
