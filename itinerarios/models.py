from django.db import models

# Create your models here.

class Itinerario(models.Model):
    nombre = models.CharField(max_length= 50)
    imagen = models.ImageField(
        upload_to='images/', 
        null=True, 
        blank=True,
        default= 'images/default.png'
)

class Parada(models.Model):
    nombre = models.CharField(max_length= 50)
    ubicacion = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 200)
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)

class PuntoDestacado(models.Model):
    nombre = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 200)
    imagen = models.ImageField()
    STATE_CHOICES = [
        ('ELIMINADO', 'Eliminado'),
        ('ACTIVO', 'Activo'),
        ('BAJA', 'Baja'),
    ]
    estado = models.CharField(max_length= 20, choices= STATE_CHOICES, default= 'ACTIVO')
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)