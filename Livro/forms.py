from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'genero']
        # Você pode personalizar os widgets aqui se precisar de campos HTML específicos
        # widgets = { 'titulo': forms.TextInput(attrs={'class': 'form-control'}) }
