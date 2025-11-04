from django.db import models
from recorridos.models import Circuito
from colectivos.models import Colectivo

# Create your models here.

class Reserva(models.Model):
    fecha = models.DateField()
    puntoPartida = models.CharField(max_length= 100)
    cantCupos = models.IntegerField()
    circuito = models.ForeignKey(Circuito, on_delete= models.CASCADE)
    colectivo = models.ForeignKey(Colectivo, 
                                    on_delete= models.CASCADE, 
                                    default= None, 
                                    null=True, 
                                    blank=True
                                )