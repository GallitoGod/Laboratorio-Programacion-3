from django.shortcuts import render
from itinerarios.models import Itinerario
from colectivos.models import Colectivo
from .models import Circuito

# Create your views here.

def recorrido_formulario(request):
    itinerarios = Itinerario.objects.all()
    colectivos = Colectivo.objects.all()
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            fecha_hora = request.POST.get('fecha')
            origen = request.POST.get('origen')
            destino = request.POST.get('destino')
            itinerario = request.POST.get('itinerario')
            colectivo = request.POST.get('colectivo')
            #Circuito.objects.create(nombre=nombre, hora=fecha_hora, origen=origen, destino=destino, itinerario=itinerario, colectivo=colectivo, estado='ACTIVO')
            respuesta = 'Se cargo el recorrido correctamente.'
            return render(request, 'recorrido_form.html', {
                'respuesta_bool': True, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios, 
                'colectivos': colectivos
            })
        except:
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