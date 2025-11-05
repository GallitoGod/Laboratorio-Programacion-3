from django.shortcuts import render, get_object_or_404, redirect
from .models import Colectivo
from .forms import ColectivoForm
from recorridos.models import Circuito
from usuarios.models import Usuario

def formulario_colectivo(request):
    usuarios = Usuario.objects.all()
    circuitos = Circuito.objects.all()

    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            cant_as = request.POST.get('cantAsientos')
            matricula = request.POST.get('matricula')
            descripcion = request.POST.get('descripcion')
            operador_pk = request.POST.get('operador')
            circuito_pk = request.POST.get('circuito')

            try:
                cantidad_asientos = int(cant_as)
            except (TypeError, ValueError):
                cantidad_asientos = 0

            if not operador_pk or not circuito_pk or cantidad_asientos <= 0:
                return redirect('colectivos:colectivo_listar')

            if not (nombre and descripcion and operador_pk and circuito_pk and matricula):
                    raise ValueError("Debe completar todos los campos obligatorios.")

            operador_obj = get_object_or_404(Usuario, pk= operador_pk)
            circuito_obj = get_object_or_404(Circuito, pk= circuito_pk)

            Colectivo.objects.create(
                nombre= nombre, 
                cant_asientos= cantidad_asientos, 
                matricula= matricula, 
                operador= operador_obj, 
                descripcion= descripcion, 
                circuito= circuito_obj,
                estado= 'ACTIVO'
            )

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print("ERROR:", e)
            
        return redirect('colectivos:coletivo_listar')
    else:
        return render(request, 'colectivo_form.html', {
            'usuarios': usuarios,
            'circuitos': circuitos
        })

def eliminar_colectivo(request, pk):
    if request.method != 'POST':
        return redirect('colectivos:colectivo_listar')
    obj = get_object_or_404(Colectivo, pk=pk)
    obj.delete()
    return redirect('colectivos:colectivo_listar')


def editar_colectivo(request, pk):
    obj = get_object_or_404(Colectivo, pk=pk)
    if request.method == 'POST':
        form = ColectivoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('colectivos:colectivo_listar')
        else:
            return render(request, 'colectivo_editar.html', {'form': form, 'obj': obj})
    else:
        form = ColectivoForm(instance=obj)
        return render(request, 'colectivo_editar.html', {'form': form, 'obj': obj})
    
def lista_colectivo(request):
    colectivos = Colectivo.objects.all()
    return render(request, 'colectivo_lista.html', {'colectivos': colectivos})