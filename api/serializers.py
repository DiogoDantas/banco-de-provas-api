from rest_framework import serializers
from .models import Prova, Curso, Disciplina, Periodo

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    curso = CursosSerializer(many=True, read_only=True)
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProvasSerializer(serializers.ModelSerializer):
    periodo = PeriodoSerializer(read_only=True)
    disciplina = DisciplinaSerializer(read_only=True)

    class Meta:
        model = Prova
        fields = '__all__'



