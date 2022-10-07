from django.db import models


# Create your models here.
class InfosTable(models.Model):
    type = models.IntegerField()
    date = models.CharField(max_length=12)
    value = models.FloatField()
    cpf = models.PositiveBigIntegerField()
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=12)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)
