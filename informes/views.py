from django.shortcuts import render, get_object_or_404
from datetime import datetime
from typing import Optional
from django.db.models import Sum, DateTimeField
from django.db.models.functions import Coalesce
from itinerarios.models import Itinerario, Parada
from recorridos.models import Circuito
from colectivos.models import Colectivo
from reservas.models import Reserva

# Create your views here.

def _d(s: Optional[str]):
    if not s:
        return None
    try:
        return datetime.strptime(s.strip(), '%Y-%m-%dT%H:%M')
    except ValueError:
        return None

def _rango(qs, desde, hasta, campo):
    if not (desde or hasta):
        return qs.none()

    field = qs.model._meta.get_field(campo)
    is_dt = isinstance(field, DateTimeField)
    base = f'{campo}__date' if is_dt else campo

    if desde:
        qs = qs.filter(**{f'{base}__gte': desde.date()})
    if hasta:
        qs = qs.filter(**{f'{base}__lte': hasta.date()})
    return qs

def informe_recorridos_activos(request):
    desde = _d(request.GET.get('desde'))
    hasta = _d(request.GET.get('hasta'))
    it_id = request.GET.get('itinerario') or None

    circuitos = Circuito.objects.filter(estado='ACTIVO').select_related('itinerario')
    if it_id:
        circuitos = circuitos.filter(itinerario_id=it_id)
    circuitos = _rango(circuitos, desde, hasta, campo='horario').order_by('horario')

    rows = []
    for c in circuitos:
        disponibles = c.cantidad_maxima_asientos  
        res_qs = _rango(Reserva.objects.filter(circuito=c), desde, hasta, campo='fecha')
        ocupados = res_qs.aggregate(p=Coalesce(Sum('cantCupos'), 0))['p']
        pct = (ocupados / disponibles * 100) if disponibles else 0
        rows.append({
            'itinerario': c.itinerario.nombre if c.itinerario_id else '',
            'circuito': c.nombre,
            'fecha_hora': c.horario,
            'asientos_disponibles': disponibles,
            'personas_reservadas': ocupados,
            'ocupacion_pct': pct,
        })

    return render(request, 'rec_activos.html', {
        'rows': rows,
        'itinerarios': Itinerario.objects.all(),
        'filtros': request.GET
    })


def informe_reservas_por_recorrido(request):
    recorrido_id = request.GET.get('recorrido')
    recorridos = Circuito.objects.all()

    reservas = None
    if recorrido_id:
        print('POR ACA ANDA')
        reservas = Reserva.objects.filter(circuito_id=recorrido_id)
        print(reservas)

    return render(request, 'rec_res.html', {
        'recorridos': recorridos,
        'reservas': reservas,
        'recorrido_seleccionado': recorrido_id
    })


def informe_paradas_mas_concurridas(request):
    it_id = request.GET.get('itinerario')
    itinerarios = Itinerario.objects.all().order_by('id')

    filas = []
    itinerario = None

    if it_id:
        itinerario = get_object_or_404(Itinerario, id=it_id)
        paradas = Parada.objects.filter(itinerario_id=it_id).order_by('id')
        reservas = Reserva.objects.filter(circuito__itinerario_id=it_id)

        conteo = {}
        for r in reservas:
            if r.puntoPartida not in conteo:
                conteo[r.puntoPartida] = r.cantCupos
            else:
                conteo[r.puntoPartida] += r.cantCupos

        for p in paradas:
            key_nombre = p.nombre
            key_repr   = str(p)
            concurrencia = conteo.get(key_nombre, 0) or conteo.get(key_repr, 0)
            filas.append({
                'parada_id': p.id,
                'parada_nombre': p.nombre,
                'concurrencia': concurrencia,
            })

    return render(request, 'par_conc.html', {
        'itinerarios': itinerarios,
        'itinerario': itinerario,
        'filas': filas,
        'it_id': it_id,
    })


def cantidad_pasajeros_por_viaje(request):
    circuitos = Circuito.objects.all().order_by('id')
    circuito_id = request.GET.get('circuito')
    desde = request.GET.get('desde')
    hasta = request.GET.get('hasta')

    total_pasajeros = 0
    reservas = []

    if circuito_id and desde and hasta:
        reservas = Reserva.objects.filter(
            circuito_id=circuito_id,
            fecha__range=[desde, hasta]
        )

        for r in reservas:
            total_pasajeros += r.cantCupos

    return render(request, 'cant_pas_v.html', {
        'circuitos': circuitos,
        'reservas': reservas,
        'total_pasajeros': total_pasajeros,
        'circuito_id': circuito_id,
        'desde': desde,
        'hasta': hasta,
    })


def informes(request):
    return render(request, 'informes.html')