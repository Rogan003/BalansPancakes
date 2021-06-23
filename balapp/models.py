from django.db import models

# Create your models here.
class Prodaja(models.Model):
    godina = models.IntegerField(default = 0)
    brojPalacinaka = models.IntegerField(default = 0)