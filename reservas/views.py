from django.shortcuts import render, get_object_or_404, redirect
from itinerarios.models import Itinerario, Parada
from recorridos.models import Circuito
from colectivos.models import Colectivo
from .models import Reserva

# Create your views here.

def reserva_formulario(request, pk):
    itinerario = Itinerario.objects.get(pk= pk)
    circuitos = Circuito.objects.filter(itinerario= itinerario).order_by('id')
    paradas = Parada.objects.filter(itinerario= itinerario).order_by('id')
    if request.method == 'POST':
        circuito_pk = request.POST.get('circuito')
        punto_partida_pk = request.POST.get('punto_partida')
        cant_per = request.POST.get('cant_per', 0)

        try:
            cantidad_personas = int(cant_per)
        except (TypeError, ValueError):
            cantidad_personas = 0

        if not circuito_pk or not punto_partida_pk or cantidad_personas <= 0:
            respuesta = 'Datos incorrectos, volver a intentar.'
            return render(request, 'reserva_form.html', {
                'respuesta_bool': False,
                'respuesta': respuesta,
                'itinerario': itinerario,
                'circuitos': circuitos,
                'paradas': paradas
            })

        circuito = get_object_or_404(Circuito, pk=circuito_pk, itinerario=itinerario)
        punto_partida = get_object_or_404(Parada, pk=punto_partida_pk, itinerario=itinerario)
        col_candidatos = (Colectivo.objects
                        .select_for_update()
                        .filter(circuito=circuito)
                    )

        elegido = None
        mejor_sobrante = None
        for col in col_candidatos:
            disponibles = col.asientos_disponibles
            if disponibles >= cantidad_personas:
                sobrante = disponibles - cantidad_personas
                if mejor_sobrante is None or sobrante < mejor_sobrante:
                    mejor_sobrante = sobrante
                    elegido = col

        if not elegido:
            respuesta = 'No Hay espacio suficiente en los colectivos del circuito.'
            return render(request, 'reserva_form.html', {
                'respuesta_bool': False,
                'respuesta': respuesta,
                'itinerario': itinerario,
                'circuitos': circuitos,
                'paradas': paradas
            })

        elegido.cant_ocupados = elegido.cant_ocupados + cantidad_personas
        elegido.save()

        Reserva.objects.create(
            fecha= circuito.horario,
            puntoPartida=punto_partida,
            cantCupos=cantidad_personas,
            circuito=circuito,
            colectivo=elegido,
        )
        return redirect('itinerarios:itinerario_detalle', pk=itinerario.pk)
    
    else:
        return render(request, 'reserva_form.html', {
            'itinerario_pk': pk,
            'circuitos': circuitos,
            'paradas': paradas
        })