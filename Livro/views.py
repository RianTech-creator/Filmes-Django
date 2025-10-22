from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def listar_livros(request):
    """
    Exibe uma lista de todos os livros cadastrados.
    """
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html', {'livros': livros})

def cadastrar_livro(request):
    """
    Permite cadastrar um novo livro.
    """
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros') # Redireciona para a lista de livros após o cadastro
    else:
        form = LivroForm() # Cria um formulário vazio para requisições GET
    return render(request, 'cadastrar_livro.html', {'form': form})
