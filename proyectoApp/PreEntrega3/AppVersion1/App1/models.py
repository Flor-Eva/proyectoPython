from django.db import models
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppVersion1.settings')

class Acceso(models.Model):
    nombre= models.CharField(max_length=40)
    usuario= models.EmailField()
    contraseña= models.IntegerField()
class Freelance(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion = models.CharField (max_length=30)
    servicios = models.CharField (max_length=200)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion} - Servicios {self.servicios}"
class Contratador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion = models.CharField (max_length=30)
    servicios = models.CharField (max_length=30)
class Servicios (models.Model):
    nombreServicio = models.CharField(max_length=30)
    rubro = models.CharField(max_length=30)
