from django.shortcuts import render
from .models import Aluno

# Create your views here.
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar.html', {'alunos': alunos})