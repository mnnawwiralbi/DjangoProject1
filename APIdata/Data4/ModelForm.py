from django.forms import ModelForm
from api.models import Member3

class ModelForms (ModelForm) :
    class Meta :
        model = Member3
        fields = ['namapertama', 'namabelakang', 'periode', 'date'] 