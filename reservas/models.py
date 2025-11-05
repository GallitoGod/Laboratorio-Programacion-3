from django.db import models
from recorridos.models import Circuito
from colectivos.models import Colectivo
from django.contrib.auth.models import User

# Create your models here.

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete= models.CASCADE, default= None, null= True)
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