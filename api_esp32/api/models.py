from django.db import models

# Create your models here.

class Esp(models.Model):
    temperatura=models.CharField(max_length=50)
    humedad=models.CharField(max_length=50)
    voltajeradiacion=models.CharField(max_length=50)
    valorradiacion=models.CharField(max_length=50)
    agua=models.CharField(max_length=50)
    