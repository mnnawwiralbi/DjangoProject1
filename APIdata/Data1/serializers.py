from rest_framework import serializers
from api.models import Member2

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member2
        fields = ['firstname', 'lastname', 'tahun', 'date']
