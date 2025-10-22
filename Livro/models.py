from django.db import models
from django.urls import reverse

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('listar_livros') # Redireciona para a lista de livros após a criação/edição