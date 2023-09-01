from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medicos(models.Model):
    apellido = models.CharField(max_length= 15)
    nombre = models.CharField(max_length= 15)
    matricula = models.IntegerField()
    profesion = models.CharField(max_length= 15)
    usuario = models.CharField(max_length= 15)
    contraseña = models.CharField(max_length= 15)
    email = models.EmailField()
    sector = models.CharField(max_length= 15)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        ordering = ['nombre']



class Personal(models.Model):
    apellido = models.CharField(max_length= 15)
    nombre = models.CharField(max_length= 15)
    email = models.EmailField()
    sector = models.CharField(max_length= 15)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal pero en plural"
        ordering = ['nombre']

class Turnos(models.Model):
    especialidad = models.CharField(max_length=15)
    turno = models.DateField()

    def __str__(self):
        return f"Usted, saco el turno para {self.especialidad}, en el dia {self.turno}"
    
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ['turno']

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"