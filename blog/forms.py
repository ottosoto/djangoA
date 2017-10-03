from django import forms
from .models import publicar

class PostearForm(forms.ModelForm):

    class Meta:
        model = publicar
        fields = ('titulo', 'texto',)
