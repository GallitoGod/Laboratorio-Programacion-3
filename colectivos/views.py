from django.shortcuts import render
from colectivos.models import Colectivo
from usuarios.models import Usuario

def formulario_colectivo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantAsientos = request.POST.get('cantAsientos')
        matricula = request.POST.get('matricula')
        descripcion = request.POST.get('descripcion')
        operador = request.POST.get('operador')
        Colectivo.objects.create(nombre=nombre, cantAsientos=cantAsientos, matricula=matricula, operador=operador, descripcion=descripcion, estado='Activo')
        return render(request, 'colectivo_form.html')
    else:
        usuarios = Usuario.objects.all()
        return render(request, 'colectivo.form.html', {'usuarios': usuarios})


