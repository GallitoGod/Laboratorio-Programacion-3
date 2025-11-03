from django.shortcuts import render
from recorridos.models import Circuito
from .models import Reserva

# Create your views here.
#TODO: una reserva se hace sobre un itinerario, mi idea es mostrar todos los itinerarios en pagina pincipal,
#si se toca, se envia a la pagina especifica de este itinerario mostrando imagen/es, descripcion, nombre, etc
#y un boton de reseva, el cual tiene que llevar a reserva_formulario, pero debe ser especifico a ese itinerario
#asi se pueden elegir los puntos de partida de los itinerarios siendo todas las paradas que contiene.

def reserva_formulario(request):
    if request.method == 'POST':
        
        return render(request, 'reserva_form.html')
    
    else:
        circuitos = Circuito.objects.all()
        #puntos_partida = circuitos.itinerario.parada_set.all()
        #print(puntos_partida)
        return render(request, 'reserva_form.html', {'circuitos':circuitos})