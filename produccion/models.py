from django.db import models
from django.contrib.auth.models import User

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Produccion(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fechahora = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(auto_now_add=True)
    operador = models.CharField(max_length=100)
    modificado_por = models.ForeignKey(User, related_name='modificado_por', null=True, blank=True, on_delete=models.SET_NULL)
    modificado_el = models.DateTimeField(null=True, blank=True)
    anulado = models.BooleanField(default=False)
    anulado_por = models.ForeignKey(User, related_name='anulado_por', null=True, blank=True, on_delete=models.SET_NULL)
    anulado_el = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.planta} - {self.producto} - {self.cantidad} - {self.fecha}"
