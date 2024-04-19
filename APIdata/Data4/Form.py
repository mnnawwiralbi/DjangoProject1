from django import forms
from .ModelForm import ModelForm

class ContactForm (forms.Form) :
    namapertama = forms.CharField(label="Mahasiswa", max_length=100)
    namabelakang = forms.CharField(widget=forms.Textarea)
    periode = forms.CharField(widget=forms.Textarea)
    date = forms.CharField(widget=forms.Textarea)
