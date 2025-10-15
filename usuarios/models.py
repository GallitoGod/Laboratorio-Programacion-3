from django.db import models

# Create your models here.
class Usuario(models.Model):
    dni = models.IntegerField()
    gmail = models.EmailField()
    nombre = models.CharField(max_length= 50)
    password = models.CharField(max_length= 50)
    ROLE_CHOICES = [
        ('TURISTA', 'Turista'),
        ('OPERADOR', 'Operador'),
        ('ADMIN', 'Admin'),
    ]
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES)

