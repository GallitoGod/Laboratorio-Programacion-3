from django.db import models
from recorridos.models import Circuito

# Create your models here.

class Reserva(models.Model):
    fecha = models.DateField()
    puntoPartida = models.CharField(max_length= 100)
    cantCupos = models.IntegerField()
    circuito = models.ForeignKey(Circuito, on_delete= models.CASCADE)