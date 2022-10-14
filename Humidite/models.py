from django.db import models

# Create your models here.from django.db import models

class Plante(models.Model):
    humidite_val = models.fields.FloatField(max_length = 5)
    unixtime_val = models.fields.IntegerField(blank=True, null=True)