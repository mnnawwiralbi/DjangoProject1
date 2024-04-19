from rest_framework import serializers
from api.models import Member3

class serializerpost (serializers.ModelSerializer) :
    class Meta :
        model = Member3
        fields = ['namapertama', 'namabelakang', 'periode', 'date']
