from django.shortcuts import render
from itinerarios.models import Itinerario
from colectivos.models import Colectivo
from .models import Circuito

# Create your views here.

def formulario_recorrido(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha_hora = request.POST.get('fecha')
        origen = request.POST.get('origen')
        destino = request.POST.get('destino')
        itinerario = request.POST.get('itinerario')
        colectivo = request.POST.get('colectivo')
        Circuito.objects.create(nombre=nombre, hora=fecha_hora, origen=origen, destino=destino, itinerario=itinerario, colectivo=colectivo, estado='ACTIVO')
        return render(request, 'recorrido_form.html')
    else:
        itinerarios = Itinerario.objects.all()
        colectivos = Colectivo.objects.all()
        return render(request, 'recorrido_form.html', {'itinerarios': itinerarios, 'colectivos': colectivos})