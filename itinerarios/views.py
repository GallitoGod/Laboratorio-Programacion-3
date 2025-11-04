from django.shortcuts import render, get_object_or_404
from .models import Itinerario, PuntoDestacado, Parada

# Create your views here.


def formulario_itinerario(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            imagen = request.FILES.get('imagen')
            Itinerario.objects.create(nombre= nombre, imagen= imagen)
            respuesta = 'Se cargo el itinerario correctamente.'
            return render(request, 'itinerario_form.html', {'respuesta_bool': True,'respuesta': respuesta})
        except:
            respuesta = 'Valores incorrectos, por favor volver a intentar.'
            return render(request, 'itinerario_form.html', {'respuesta_bool': False, 'respuesta': respuesta})
    else:
        return render(request, 'itinerario_form.html')
    
def formulario_punto_destacado(request):
    itinerarios = Itinerario.objects.all()
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            imagen = request.FILES.get('imagen')
            itinerario = request.POST.get('itinerario')
            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario)
            PuntoDestacado.objects.create(nombre= nombre, descripcion=descripcion, imagen= imagen, estado='ACTIVO', itinerario= itinerario_obj)
            respuesta = 'Se cargo el punto destacado correctamente.'
            return render(request, 'pd_form.html', {
                'respuesta_bool': False, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios
            })
        except Exception as e:
            print('ERROR:', e)
            respuesta = 'Valores incorrectos, por favor volver a intentar.'
            return render(request, 'pd_form.html', {
                'respuesta_bool': False, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios
            })
    else:
        print('entrando a la vista de puntos destacados')
        return render(request, 'pd_form.html', {'itinerarios': itinerarios})
    
def formulario_parada(request):
    itinerarios = Itinerario.objects.all()
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            ubicacion = request.POST.get('ubicacion')
            descripcion = request.POST.get('descripcion')
            itinerario = request.POST.get('itinerario')
            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario)
            Parada.objects.create(nombre= nombre, ubicacion= ubicacion, descripcion=descripcion, itinerario= itinerario_obj)
            respuesta = 'Se cargo la parada correctamente.'
            return render(request, 'parada_form.html', {
                'respuesta_bool': True,
                'respuesta': respuesta, 
                'itinerarios': itinerarios
            })
        except:
            respuesta = 'Valores incorrectos, por favor volver a intentar.'
            return render(request, 'parada_form.html', {
                'respuesta_bool': False, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios
            })
    else:
        return render(request, 'parada_form.html', {'itinerarios': itinerarios})
    

def detalles_itinerario(request, pk):
    itinerario = Itinerario.objects.get(pk= pk)
    puntos_destacados = PuntoDestacado.objects.filter(itinerario= itinerario)
    paradas = Parada.objects.filter(itinerario= itinerario).order_by('id')
    return render(request, 'itinerario_detalle.html', {
        'itinerario': itinerario,
        'puntos_destacados': puntos_destacados,
        'paradas': paradas
        })