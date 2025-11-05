from django import forms
from .models import Circuito

class CircuitoForm(forms.ModelForm):
    class Meta:
        model = Circuito
        fields = [
            'nombre', 
            'horario',
            'origen',
            'destino',
            'itinerario',
            'estado',
        ]