from django.db import models

# Create your models here.

class Itinerario(models.Model):
    id = models.CharField(max_length= 50, primary_key= True)
    nombre = models.CharField(max_length= 50)

class Parada(models.Model):
    id = models.CharField(max_length= 50, primary_key= True)
    nombre = models.CharField(max_length= 50)
    ubicacion = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 200)
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)

class PuntoDestacado(models.Model):
    id = models.CharField(max_length= 50, primary_key= True)
    nombre = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 200)
    imagen = models.ImageField()
    itinerario = models.ForeignKey(Itinerario, on_delete= models.CASCADE)