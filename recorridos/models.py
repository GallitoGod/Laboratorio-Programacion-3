from django.db import models
from itinerarios.models import Itinerario
from colectivos.models import Colectivo

# Create your models here.

class Circuito(models.Model):
    nombre = models.CharField(max_length= 50)
    horario = models.TimeField()
    origen = models.CharField(max_length= 50, default='sin origen')
    destino = models.CharField(max_length= 50, default= 'sin destino')
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)
    colectivo = models.ForeignKey(Colectivo, on_delete= models.CASCADE)
    STATE_CHOICES = [
        ('ELIMINADO', 'Eliminado'),
        ('ACTIVO', 'Activo'),
        ('BAJA', 'Baja'),
    ]
    estado = models.CharField(max_length= 20, choices= STATE_CHOICES, default= 'ACTIVO')