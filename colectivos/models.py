from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Colectivo(models.Model):
    nombre = models.CharField(max_length= 20, default= 'sin nombre')
    cantAsientos = models.IntegerField()
    matricula = models.CharField(max_length= 20)
    operador = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    descripcion = models.TextField(max_length= 200, default= 'sin descripcion')
    STATE_CHOICES = [
        ('ELIMINADO', 'Eliminado'),
        ('ACTIVO', 'Activo'),
        ('BAJA', 'Baja'),
    ]
    estado = models.CharField(max_length= 20, choices= STATE_CHOICES, default='ACTIVO')