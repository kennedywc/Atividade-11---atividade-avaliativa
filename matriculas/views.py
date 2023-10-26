from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def listar_alunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos:listar_alunos')
    else:
        form = AlunoForm()

    alunos = Aluno.objects.all()
    return render(request, 'listar.html', {'alunos': alunos, 'form': form})