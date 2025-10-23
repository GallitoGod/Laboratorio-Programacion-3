from django.shortcuts import render

# Create your views here.

def formulario_recorrido(request):
    return render(request, 'recorrido_form.html')