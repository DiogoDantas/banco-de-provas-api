from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from api.serializers import ProvasSerializer, CursosSerializer, DisciplinaSerializer, PeriodoSerializer
from .models import Prova, Curso, Disciplina, Periodo
from django_filters.rest_framework import DjangoFilterBackend
 
# Create your views here.

@api_view(['GET'])
def index(request, format=None):
    return Response({
       'api': 'BancoDeProvasUFPB',
       'version': '0.0.1',
    })


class SearchMixin():
	
	keydict = {
		'disciplina':'disciplina',
	}	

	@classmethod
	def filter(self, cls, key):
		per = cls.objects.filter(id=key)
		if(key is None):
			return Prova.objects.all()
		else:
			return  Prova.objects.filter(disciplina=per)



class ProvasViewSet(viewsets.ModelViewSet):
	queryset = Prova.objects.all()
	serializer_class = ProvasSerializer
	
	def get_queryset(self):
		params = self.request.query_params
		if len(params) == 0:
			return Prova.objects.all()
		else:			
			disciplina = params.get('disciplina',None)
			print("Disciplina={0}".format(disciplina))
			classificacao = params.get('classificacao',None)
			curso = params.get('curso',None)
			periodo = params.get('periodo',None)
			print("Periodo={0}".format(periodo))

			provas = Prova.objects.all()

			if(curso is not None):
				#curso = Curso.objects.filter(id=curso)
				#disciplinas = Disciplina.objects.filter(curso=curso)
				provas = provas.filter(disciplina__curso__id=curso)
			if(disciplina is not None):
				provas = provas.filter(disciplina__id=disciplina)
			if(periodo is not None):	
				provas = provas.filter(periodo__id=periodo)
			if(classificacao is not None):	
				provas = provas.filter(classificacao__gte=classificacao)	
					
			return provas

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