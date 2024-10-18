from django.db import models

class Mesa(models.Model):
    num_mesa = models.PositiveBigIntegerField()

    def __str__(self):
        return f"la mesa {self.num_mesa}"




