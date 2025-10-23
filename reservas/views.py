from django.shortcuts import render

# Create your views here.

def reserva_formulario(request):
    return render(request, 'reserva_form.html')