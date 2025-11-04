from django.shortcuts import render, get_object_or_404
from .models import Itinerario, PuntoDestacado, Parada

# Create your views here.


def formulario_itinerario(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            imagen = request.FILES.get('imagen')

            if not nombre:
                raise ValueError("Debe ingresar un nombre para el itinerario.")

            Itinerario.objects.create(nombre= nombre, imagen= imagen)
            respuesta_bool = True
            respuesta = 'Se cargo el itinerario correctamente.'

        except ValueError as ve:
            respuesta_bool = False
            respuesta = f"Error: {ve}"

        except Exception as e:
            print("ERROR:", e)
            respuesta_bool = False
            respuesta = "Error al cargar el itinerario."
        
        return render(request, 'itinerario_form.html', {
            'respuesta_bool': respuesta_bool,
            'respuesta': respuesta
        })
    
    else:
        return render(request, 'itinerario_form.html')
    
def formulario_punto_destacado(request):
    itinerarios = Itinerario.objects.all()
    
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            imagen = request.FILES.get('imagen')
            itinerario_pk = request.POST.get('itinerario')

            if not (nombre and descripcion and itinerario_pk):
                raise ValueError("Debe completar todos los campos obligatorios.")

            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario_pk)

            PuntoDestacado.objects.create(
                nombre= nombre, 
                descripcion=descripcion, 
                imagen= imagen, 
                estado='ACTIVO', 
                itinerario= itinerario_obj
            )

            respuesta_bool = True
            respuesta = 'Se cargo el punto destacado correctamente.'

        except ValueError as ve:
            respuesta_bool = False
            respuesta = f"Error: {ve}"

        except Exception as e:
            print("ERROR:", e)
            respuesta_bool = False
            respuesta = "Error inesperado al cargar el punto destacado."

        return render(request, 'pd_form.html', {
            'respuesta_bool': respuesta_bool,
            'respuesta': respuesta,
            'itinerarios': itinerarios
        })
    
    else:
        return render(request, 'pd_form.html', {'itinerarios': itinerarios})
    
def formulario_parada(request):
    itinerarios = Itinerario.objects.all()

    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            ubicacion = request.POST.get('ubicacion')
            descripcion = request.POST.get('descripcion')
            itinerario_pk = request.POST.get('itinerario')

            if not (nombre and ubicacion and descripcion and itinerario_pk):
                raise ValueError("Debe completar todos los campos obligatorios.")

            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario_pk)

            Parada.objects.create(
                nombre= nombre, 
                ubicacion= ubicacion, 
                descripcion=descripcion, 
                itinerario= itinerario_obj
            )

            respuesta_bool = True
            respuesta = 'Se cargo la parada correctamente.'
        
        except ValueError as ve:
            respuesta_bool = False
            respuesta = f"Error: {ve}"

        except Exception as e:
            print("ERROR:", e)
            respuesta_bool = False
            respuesta = "Error inesperado al cargar la parada."

        return render(request, 'parada_form.html', {
            'respuesta_bool': respuesta_bool,
            'respuesta': respuesta,
            'itinerarios': itinerarios
        })
    
    else:
        return render(request, 'parada_form.html', {'itinerarios': itinerarios})
    

def detalles_itinerario(request, pk):
    try:
        itinerario = get_object_or_404(Itinerario, pk=pk)
        puntos_destacados = PuntoDestacado.objects.filter(itinerario=itinerario)
        paradas = Parada.objects.filter(itinerario=itinerario).order_by('id')

        return render(request, 'itinerario_detalle.html', {
            'itinerario': itinerario,
            'puntos_destacados': puntos_destacados,
            'paradas': paradas
        })

    except Itinerario.DoesNotExist:
        print("ERROR: el itinerario solicitado no existe.")
        return render(request, 'itinerario_detalle.html', {
            'error': "El itinerario solicitado no existe."
        })

    except Exception as e:
        print("ERROR:", e)
        return render(request, 'itinerario_detalle.html', {
            'error': "Error al cargar el detalle del itinerario."
        })