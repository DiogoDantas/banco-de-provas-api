from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Disciplina(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=150)

	def __str__(self):
		return self.nome

class Curso(models.Model):
	id = models.AutoField(primary_key=True)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
	nome = models.CharField(max_length=150)

	def __str__(self):
		return self.nome


class Prova(models.Model):
    id = models.AutoField(primary_key=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=100, blank=True, default='')
    data_upload = models.DateTimeField(auto_now_add=True)
    classificacao = models.IntegerField()
    miniatura = models.TextField()
    pdf_path = models.TextField()

    def __str__(self):
    	return str(self.disciplina) + ' ' + self.periodo
