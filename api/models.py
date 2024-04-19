from django.db import models

# Create your models here.

class Member2(models.Model):
  firstname = models.CharField(primary_key=True, max_length=10)
  lastname = models.CharField(max_length=255)
  tahun = models.IntegerField()
  date = models.DateField()

  def __str__(self):
        return self.firstname

class Member3(models.Model):
  namapertama = models.CharField(primary_key=True, max_length=10)
  namabelakang = models.CharField(max_length=255)
  periode = models.IntegerField()
  date = models.DateField()

  def __str__(self):
        return self.namapertama

class Login(models.Model):
  userid = models.CharField(primary_key=True, max_length=10)
  user = models.CharField(max_length=255, null=True)
  password = models.CharField(max_length=250, null=True)
  email = models.CharField(max_length=100, null=True)
  date = models.DateField()

  def __str__(self):
        return self.namapertama
  
