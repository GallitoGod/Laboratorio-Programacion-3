from django.db import models
from itinerarios.models import Itinerario
from colectivos.models import Colectivo

# Create your models here.

class Circuito(models.Model):
    id = models.CharField(max_length= 50, primary_key= True)
    nombre = models.CharField(max_length= 50)
    horario = models.TimeField()
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)
    colectivo = models.ForeignKey(Colectivo, on_delete= models.CASCADE)