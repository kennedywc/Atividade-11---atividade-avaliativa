from django.urls import path, include
from matriculas import views

urlpatterns = [
    path('', views.listar_alunos, name='listar'),
]