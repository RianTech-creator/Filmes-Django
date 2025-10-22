from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('', views.listar_livros, name='listar_livros'),
]