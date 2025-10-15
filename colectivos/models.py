from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Colectivo(models.Model):
    cantAsientos = models.IntegerField()
    matricula = models.CharField(max_length= 20)
    operador = models.ForeignKey(Usuario, on_delete= models.CASCADE)