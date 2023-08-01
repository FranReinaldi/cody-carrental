from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField(blank=True,null=True)