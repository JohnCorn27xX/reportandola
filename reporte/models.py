from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creacion = models.DateField(auto_now_add=True)
    encargado = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Tipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Copiadora(models.Model):
    nombre = models.CharField(max_length=100)
    Tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    Bandeja = models.IntegerField(default='1')

    def __str__(self):
       return f'{self.nombre} Bandeja {self.Bandeja}'
    
class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=100)
    dirrecion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ciudad} - {self.dirrecion}'
    
class Equipo_Sitio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    copiadora = models.ForeignKey(Copiadora, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    encargado = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    libreta = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cliente} - {self.departamento} - {self.ubicacion} - {self.copiadora}'