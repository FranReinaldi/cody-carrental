from django.db import models

class Manufacturer(models.Model):
    name = models.CharField()

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField()
    year = models.IntegerField(blank=True,null=True)