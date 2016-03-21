from django.db import models

# Create your models here.
class Puesto(models.Model):
    puesto=models.CharField(max_length=20)

class Persona(models.Model):
    ap_paterno=models.CharField(max_length=20)
    ap_materno=models.CharField(max_length=20)
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    email=models.EmailField()
    distrito=models.CharField(max_length=20)
    puesto=models.ForeignKey(Puesto,null=True)
    class Meta():
        abstract=True

class Empleado(Persona):
    salario=models.DecimalField(max_digits=8,decimal_places=2)
    dni=models.IntegerField()
    usuario=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    fec_nac=models.DateField()
    fec_ing=models.DateField()

class Cliente(Persona):
    pass

class Especie(models.Model):
    especie=models.CharField(max_length=30)

class Raza(models.Model):
    raza=models.CharField(max_length=20)
    especie=models.ForeignKey(Especie)

class Mascota(models.Model):
    nombre=models.CharField(max_length=20)
    sexo=models.CharField(max_length=10)
    fec_nac=models.DateField()
    intacto=models.CharField(max_length=10)
    castrado=models.CharField(max_length=10)
    fec_castracion=models.DateField()
    raza=models.ForeignKey(Raza)
    cliente=models.ForeignKey(Cliente)
