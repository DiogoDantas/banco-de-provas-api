from django.db import models

class Periodo(models.Model):
    semestre = models.CharField(max_length=10)

    def __str__(self):
        return self.semestre


class Curso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    curso = models.ManyToManyField(Curso)
    
    def __str__(self):
        return self.nome

class Prova(models.Model):
    pdf = models.FileField()
    miniatura = models.ImageField(blank=True, null=True)
    data_upload = models.DateTimeField(auto_now_add=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    classificacao = models.IntegerField()

    def __str__(self):
        return str(self.disciplina)
