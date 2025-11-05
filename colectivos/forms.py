from django import forms
from .models import Colectivo

class ColectivoForm(forms.ModelForm):
    class Meta:
        model = Colectivo
        fields = [
            'nombre', 
            'cant_asientos', 
            'matricula',
            'operador',
            'descripcion',
            'circuito',
            'estado',
        ]