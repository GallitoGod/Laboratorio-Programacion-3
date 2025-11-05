from django import forms
from .models import Itinerario, Parada, PuntoDestacado

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = [
            'nombre', 
            'imagen', 
        ]

class ParadaForm(forms.ModelForm):
    class Meta:
        model = Parada
        fields = [
            'nombre',
            'ubicacion',
            'descripcion',
            'itinerario'
        ]

class PDestacadoForm(forms.ModelForm):
    class Meta:
        model = PuntoDestacado
        fields = [
            'nombre',
            'descripcion',
            'imagen',
            'estado',
            'itinerario'
        ]