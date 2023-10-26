from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    data_de_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
