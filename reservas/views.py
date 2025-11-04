from django.shortcuts import render, get_object_or_404
from itinerarios.models import Itinerario, Parada
from recorridos.models import Circuito
from colectivos.models import Colectivo
from .models import Reserva

# Create your views here.
#TODO: una reserva se hace sobre un itinerario, mi idea es mostrar todos los itinerarios en pagina pincipal,
#si se toca, se envia a la pagina especifica de este itinerario mostrando imagen/es, descripcion, nombre, etc
#y un boton de reseva, el cual tiene que llevar a reserva_formulario, pero debe ser especifico a ese itinerario
#asi se pueden elegir los puntos de partida de los itinerarios siendo todas las paradas que contiene.

def reserva_formulario(request, pk):
    itinerario = Itinerario.objects.get(pk= pk)
    circuitos = Circuito.objects.filter(itinerario= itinerario).order_by('id')
    paradas = Parada.objects.filter(itinerario= itinerario).order_by('id')
    if request.method == 'POST':
        circuito_pk = request.POST.get('circuito')
        punto_partida_pk = request.POST.get('punto_partida')
        cantidad_personas = request.POST.get('cant_per')
        if cantidad_personas > 
        circuito = Circuito.objects.filter(pk= circuito_pk)
        punto_partida = Parada.objects.filter(pk= punto_partida_pk)


        return render(request, 'reserva_form.html', {
            'itinerario_pk': pk,
            'circuitos': circuitos,
            'paradas': paradas
        })
    
    else:
        return render(request, 'reserva_form.html', {
            'itinerario_pk': pk,
            'circuitos': circuitos,
            'paradas': paradas
        })
    
# def prueba():
#     circuito = get_object_or_404(Circuito, pk= 3)
#     colectivos = circuito.colectivo_set.all()
#     asientos_disponibles_por_circuito = 0
#     for colectivo in colectivos:
#         asientos_disponibles_por_circuito += colectivo.asientos_disponibles
#     print(asientos_disponibles_por_circuito)