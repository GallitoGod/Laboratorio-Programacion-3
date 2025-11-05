from django.shortcuts import render
from datetime import datetime
from typing import Optional
from django.db.models import Sum, Count, DateTimeField
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


def Todas_las_reservas_de_un_circuitoHAYQUEHACERLOTODAVIA(request):
    desde = _d(request.GET.get('desde'))
    hasta = _d(request.GET.get('hasta'))
    it_id = request.GET.get('itinerario') or None

    reservas = _rango(Reserva.objects.select_related('circuito','circuito__itinerario'),
                      desde, hasta, campo='fecha')
    if it_id:
        reservas = reservas.filter(circuito__itinerario_id=it_id)

    data = (reservas
            .values('circuito__itinerario__nombre', 'circuito__nombre')
            .annotate(reservas=Count('id'),
                      personas=Coalesce(Sum('cantCupos'), 0))
            .order_by('circuito__itinerario__nombre', 'circuito__nombre'))

    return render(request, 'reportes/rf25.html', {
        'rows': data,
        'itinerarios': Itinerario.objects.all(),
        'filtros': request.GET
    })