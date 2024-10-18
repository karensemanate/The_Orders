from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.nombre
