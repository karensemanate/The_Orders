from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.nombre

