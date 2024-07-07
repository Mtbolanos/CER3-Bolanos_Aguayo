from django.db import models
from django.contrib.auth.models import User
from datetime import time

class Planta(models.Model):
    codigo = models.CharField(max_length=10, default=0)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=3, unique=True, default=0)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.nombre

class Produccion(models.Model):
    TURNOS = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    litros = models.PositiveIntegerField(default=0)
    fecha = models.DateField()
    turno = models.CharField(max_length=2, choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')], default='')
    hora_registro = models.TimeField(default=time(0, 0))
    operador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.nombre} - {self.fecha} - {self.turno}'
