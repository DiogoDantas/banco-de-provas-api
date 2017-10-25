from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
# Create your views here.

@api_view(['GET'])
def index(request, format=None):
    return Response({
       'users': 'Diogo',
       'todos': 'AlgumaCoisa',
    })

@api_view(['GET'])
def get_provas(request):
	provas = Provas.objects.all()
	serializer = ProvasSerializer(provas, many=True)
	return Response(serializer.data)
	