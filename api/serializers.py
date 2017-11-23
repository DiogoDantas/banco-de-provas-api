from rest_framework import serializers
from .models import Prova, Curso, Disciplina, Periodo

class ProvasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prova
		fields = '__all__'

class CursosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Curso
		fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Disciplina
		fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Periodo
		fields = '__all__'