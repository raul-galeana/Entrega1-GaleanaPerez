from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    duenio = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Duenio: {self.duenio} - Edad: {self.edad}'