from django.shortcuts import render, get_object_or_404, redirect
from itinerarios.models import Itinerario
from colectivos.models import Colectivo
from .models import Circuito
from .forms import CircuitoForm
from datetime import datetime

# Create your views here.

def recorrido_formulario(request):
    itinerarios = Itinerario.objects.all()
    colectivos = Colectivo.objects.all()
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            fecha_str = request.POST.get('fecha')  
            fecha_hora = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
            origen = request.POST.get('origen')
            destino = request.POST.get('destino')
            itinerario_pk = request.POST.get('itinerario')

            if not (nombre and fecha_str and origen and destino and itinerario_pk):
                raise ValueError("Faltan campos obligatorios en el formulario.")
            
            try:
                fecha_hora = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                raise ValueError("El formato de fecha y hora es incorrecto.")

            itinerario_obj = get_object_or_404(Itinerario, pk=itinerario_pk)
            try:
                Circuito.objects.create(
                    nombre=nombre,
                    horario=fecha_hora,
                    origen=origen,
                    destino=destino,
                    itinerario=itinerario_obj,
                    estado='ACTIVO'
                )
            except Exception as e:
                raise RuntimeError(f"No se pudo crear el circuito: {e}")
            
            respuesta_bool = True
            respuesta = 'Se cargo el recorrido correctamente.'

            return render(request, 'recorrido_form.html', {
                'respuesta_bool': respuesta_bool, 
                'respuesta': respuesta, 
                'itinerarios': itinerarios, 
                'colectivos': colectivos
            })
        

        except ValueError as ve:
            respuesta_bool = False
            respuesta = f'Error de validacion: {ve}'

        except RuntimeError as re:
            respuesta_bool = False
            respuesta = f'Error al crear el circuito: {re}'

        except Exception as e:
            print('ERROR:', e)
            respuesta_bool = False
            respuesta = 'Ocurrio un error al procesar el formulario.'

        return render(request, 'recorrido_form.html', {
            'respuesta_bool': respuesta_bool,
            'respuesta': respuesta,
            'itinerarios': itinerarios,
            'colectivos': colectivos
        })
    
    else:
        return render(request, 'recorrido_form.html', {
            'itinerarios': itinerarios, 
            'colectivos': colectivos
        })
    
def eliminar_circuito(request, pk):
    if request.method != 'POST':
        return redirect('recorridos:circuito_listar')
    try:
        obj = get_object_or_404(Circuito, pk=pk)
        obj.delete()
        return redirect('recorridos:circuito_listar')
    except Exception as e:
        print('ERROR: ', e)
        return redirect('recorridos:circuito_listar')



def editar_circuito(request, pk):
    obj = get_object_or_404(Circuito, pk=pk)
    if request.method == 'POST':
        form = CircuitoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('recorridos:circuito_listar')
        else:
            return render(request, 'recorrido_editar.html', {'form': form, 'obj': obj})
    else:
        form = CircuitoForm(instance=obj)
        return render(request, 'recorrido_editar.html', {'form': form, 'obj': obj})
    
def lista_circuito(request):
    circuitos = Circuito.objects.all()
    return render(request, 'recorrido_lista.html', {'circuitos': circuitos})