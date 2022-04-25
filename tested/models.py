from statistics import mode
from django.db import models

class Tested(models.Model):
    name = models.CharField(max_length=140)
    thought = models.CharField(max_length=120)
