from django.shortcuts import render, get_object_or_404, redirect
from .models import Itinerario, PuntoDestacado, Parada
from .forms import ItinerarioForm, ParadaForm, PDestacadoForm

# Create your views here.


def formulario_itinerario(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            imagen = request.FILES.get('imagen')

            if not nombre:
                raise ValueError("Debe ingresar un nombre para el itinerario.")

            Itinerario.objects.create(nombre= nombre, imagen= imagen)

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print("ERROR:", e)
        
        return redirect('itinerarios:itinerario_listar')
    
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

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print("ERROR:", e)

        return redirect('itinerarios:pd_listar')
    
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

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print("ERROR:", e)

        return redirect('itinerarios:itinerario_listar')
    
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
    

def eliminar_itinerario(request, pk):
    if request.method != 'POST':
        return redirect('itinerarios:itinerario_listar')
    obj = get_object_or_404(Itinerario, pk=pk)
    obj.delete()
    return redirect('itinerarios:itinerario_listar')

def editar_itinerario(request, pk):
    obj = get_object_or_404(Itinerario, pk=pk)
    if request.method == 'POST':
        form = ItinerarioForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('itinerarios:itinerario_listar')
        else:
            return render(request, 'itinerario_editar.html', {'form': form, 'obj': obj})
    else:
        form = ItinerarioForm(instance=obj)
        return render(request, 'itinerario_editar.html', {'form': form, 'obj': obj})
    
def lista_itinerario(request):
    itinerarios = Itinerario.objects.all()
    return render(request, 'itinerario_lista.html', {'itinerarios': itinerarios})



def eliminar_parada(request, pk):
    if request.method != 'POST':
        return redirect('itinerarios:parada_listar')
    obj = get_object_or_404(Parada, pk=pk)
    obj.delete()
    return redirect('itinerarios:parada_listar')

def editar_parada(request, pk):
    obj = get_object_or_404(Parada, pk=pk)
    if request.method == 'POST':
        form = ParadaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('itinerarios:parada_listar')
        else:
            return render(request, 'parada_editar.html', {'form': form, 'obj': obj})
    else:
        form = ParadaForm(instance=obj)
        return render(request, 'parada_editar.html', {'form': form, 'obj': obj})
    
def lista_parada(request):
    paradas = Parada.objects.all()
    return render(request, 'parada_lista.html', {'paradas': paradas})



def eliminar_punto_destacado(request, pk):
    if request.method != 'POST':
        return redirect('itinerarios:pd_listar')
    obj = get_object_or_404(PuntoDestacado, pk=pk)
    obj.delete()
    return redirect('itinerarios:pd_listar')

def editar_punto_destacado(request, pk):
    obj = get_object_or_404(PuntoDestacado, pk=pk)
    if request.method == 'POST':
        form = PDestacadoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('itinerarios:pd_listar')
        else:
            return render(request, 'pd_editar.html', {'form': form, 'obj': obj})
    else:
        form = PDestacadoForm(instance=obj)
        return render(request, 'pd_editar.html', {'form': form, 'obj': obj})
    
def lista_punto_destacado(request):
    pun_destacados = PuntoDestacado.objects.all()
    return render(request, 'pd_lista.html', {'pun_destacados': pun_destacados})