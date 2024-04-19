"""
URL configuration for go project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers
from django.views.generic.base import RedirectView
from APIdata.Data3.views import delete2
from APIdata.Data4.View import contact_view 
from Controller.ControllerLogin.Controller_login import Logins
from Controller.ControllerLogout.Controller_logout import logout
from Controller.ControllerSignUp import Controller_SignUp 

urlpatterns = [
    path('', RedirectView.as_view(url='/public/', permanent=True)),
    path('public/', views.my_view, name = 'nama' ),
    path('api/', include('api.urls')),
    path('post/', include('APIdata.Data2.urls')),
    path('post/', RedirectView.as_view(url='/public/', permanent=True)),
    path('delete/', delete2, name = 'Member2'),
    path('login/', views.Login),
    path('form/', contact_view, name='kontakList'),
    path('logout/', logout),
    path('SignUp/', views.SignUp),
    path('ControllerLogin/',Logins, name="Controller_Login"),
    path('ControllerSignUp/', Controller_SignUp.SignUp, name="Controller_SignUp"),
]

#'delete/<int:id>/', delete2, name='delete_view_name'