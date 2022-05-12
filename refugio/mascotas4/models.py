from django.db import models
from django.forms import ModelForm
# Create your models here.


class usuario_solicitud(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    correo=models.EmailField()
    telefono=models.CharField(max_length=8)
    domicilio=models.CharField(max_length=250)
    numero_mascotas=models.IntegerField(default=1)
    motivo_solicitud=models.CharField(max_length=250)
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

class  Vacunas(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

class Mascota(models.Model):
    #id=models.AutoField(primary_key=True)
    nombre_mascota=models.CharField(max_length=100)
    sexo=models.CharField(max_length=10)
    edad_aproximada=models.IntegerField()
    fecha_rescate=models.DateField()
    #fotografia=models.CharField(max_length=500)
    persona=models.ForeignKey(usuario_solicitud, null=True, on_delete=models.CASCADE)
    vacuna=models.ManyToManyField(Vacunas)