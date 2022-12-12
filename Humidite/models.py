from django.db import models

class Plante(models.Model):
    id = models.AutoField(primary_key=True)
    ts = models.IntegerField(null=True)
    temperature_val = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    humidite_val = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    