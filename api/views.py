from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers import ProvasSerializer, CursosSerializer, DisciplinaSerializer, PeriodoSerializer
from .models import Prova, Curso, Disciplina, Periodo
 
# Create your views here.

@api_view(['GET'])
def index(request, format=None):
    return Response({
       'api': 'BancoDeProvasUFPB',
       'version': '0.0.1',
    })


class ProvasViewSet(viewsets.ModelViewSet):
	queryset = Prova.objects.all()
	serializer_class = ProvasSerializer

	def incrementar_classificacao_prova(self, request, pk):
		print(pk)
		queryset = Prova.objects.all()
		prova = get_object_or_404(queryset, pk=pk)
		prova.classificacao += 1
		prova.save()
		return Response({
       		'status': 'classificação atualizada'
    	})




class CursosViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursosSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
	queryset = Disciplina.objects.all()
	serializer_class = DisciplinaSerializer

class PeriodosViewSet(viewsets.ModelViewSet):
	queryset = Periodo.objects.all()
	serializer_class = PeriodoSerializer