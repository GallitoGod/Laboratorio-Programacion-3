from django.shortcuts import render, get_object_or_404
from colectivos.models import Colectivo
from usuarios.models import Usuario

def formulario_colectivo(request):
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            cant_as = request.POST.get('cantAsientos')
            matricula = request.POST.get('matricula')
            descripcion = request.POST.get('descripcion')
            operador_pk = request.POST.get('operador')

            try:
                cantidad_asientos = int(cant_as)
            except (TypeError, ValueError):
                cantidad_asientos = 0

            if not operador_pk or cantidad_asientos <= 0:
                respuesta_bool = False
                respuesta = 'Datos incorrectos, volver a intentar.'
                return render(request, 'colectivo_form.html', {
                    'respuesta_bool': respuesta_bool,
                    'respuesta': respuesta,
                    'usuarios': usuarios
                })

            if not (nombre and descripcion and operador_pk and matricula):
                    raise ValueError("Debe completar todos los campos obligatorios.")

            operador_obj = get_object_or_404(Usuario, pk= operador_pk)

            Colectivo.objects.create(
                nombre= nombre, 
                cant_asientos= cantidad_asientos, 
                matricula= matricula, 
                operador= operador_obj, 
                descripcion= descripcion, 
                estado= 'Activo'
            )

            respuesta_bool = True
            respuesta = 'Se cargo el colectivo correctamente.'
            
        except ValueError as ve:
            respuesta_bool = False
            respuesta = f"Error: {ve}"

        except Exception as e:
            print("ERROR:", e)
            respuesta_bool = False
            respuesta = "Error inesperado al cargar la parada."
            
        return render(request, 'colectivo_form.html', {
            'respuesta_bool': respuesta_bool,
            'respuesta': respuesta,
            'usuarios': usuarios
        })
    else:
        return render(request, 'colectivo_form.html', {
            'usuarios': usuarios
        })


