from django.db import models
from usuarios.models import Usuario
from recorridos.models import Circuito

# Create your models here.

class Colectivo(models.Model):
    nombre = models.CharField(max_length= 20, default= 'sin nombre')
    cant_asientos = models.IntegerField()
    cant_ocupados = models.IntegerField(default= 0)
    matricula = models.CharField(max_length= 20)
    operador = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    descripcion = models.TextField(max_length= 200, default= 'sin descripcion')
    circuito = models.ForeignKey(Circuito, 
                                    on_delete= models.CASCADE, 
                                    default= None, 
                                    null=True, 
                                    blank=True
                                )
    STATE_CHOICES = [
        ('ELIMINADO', 'Eliminado'),
        ('ACTIVO', 'Activo'),
        ('BAJA', 'Baja'),
    ]
    estado = models.CharField(max_length= 20, choices= STATE_CHOICES, default='ACTIVO')

    @property
    def asientos_disponibles(self):
        return self.cant_asientos - self.cant_ocupados