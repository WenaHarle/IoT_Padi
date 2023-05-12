from django.db import models

# Create your models here.
class Data(models.Model):
        day = models.IntegerField()
        total = models.IntegerField()
        avg = models.CharField(max_length=18)
        max = models.FloatField()
        min = models.CharField(max_length=20)
        sumD = models.IntegerField()

