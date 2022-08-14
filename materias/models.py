from django.db import models

# Create your models here.

import os

class materia(models.Model):

    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    horas_au = models.IntegerField()
    horas_cl = models.IntegerField()
