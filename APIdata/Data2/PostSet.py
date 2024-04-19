from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from .sereliezers import serializerpost
from api.models import Member3

@api_view(['POST'])
def add_data (request) :
        serializer = serializerpost(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#