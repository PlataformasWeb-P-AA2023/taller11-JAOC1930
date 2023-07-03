from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_Edificio= (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
    )


    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
        choices = opciones_tipo_Edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

class Departamento(models.Model):
    nombrePropietario = models.CharField(max_length=30)
    costo = models.FloatField()
    num_cuartos = models.IntegerField()

    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="Departamentos")

    def __str__(self):
        return "%s %s %d %s" % (self.nombrePropietario,
                self.costo,
                self.num_cuartos,
                self.edificio)

