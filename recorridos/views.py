from django.shortcuts import render, get_object_or_404
from itinerarios.models import Itinerario
from colectivos.models import Colectivo
from .models import Circuito
from datetime import datetime

# Create your views here.

def recorrido_formulario(request):
    itinerarios = Itinerario.objects.all()
    colectivos = Colectivo.objects.all()
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            fecha_str = request.POST.get('fecha')  
            fecha_hora = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
            origen = request.POST.get('origen')
            destino = request.POST.get('destino')
            itinerario_pk = request.POST.get('itinerario')
            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario_pk)
            Circuito.objects.create(nombre=nombre, horario=fecha_hora, origen=origen, destino=destino, itinerario=itinerario_obj, estado='ACTIVO')
            respuesta = 'Se cargo el recorrido correctamente.'
            return render(request, 'recorrido_form.html', {
                'respuesta_bool': True, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios, 
                'colectivos': colectivos
            })
        except Exception as e:
            print('ERROR', e)
            respuesta = 'Valores incorrectos, por favor volver a intentar.'
            return render(request, 'recorrido_form.html', {
                'respuesta_bool': False, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios, 
                'colectivos': colectivos
            })
    else:
        return render(request, 'recorrido_form.html', {
            'itinerarios': itinerarios, 
            'colectivos': colectivos
        })