from django.shortcuts import render
from itinerarios.models import Itinerario

# Create your views here.
#Aca tiene que estar todos los itinearios como cartitas pinchables para acceder a sus atributos y poder reservar desde ellas...


def home(request):
    return render(request, 'landing_page.html') 