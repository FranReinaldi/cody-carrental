from django.db import models
from applications.users.models import CustomUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField(blank=True,null=True)
    daily_price = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.year}'

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    calification = models.IntegerField(blank=True,null=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,blank=True)

    def get_price(self):
        return (self.end_date - self.start_date).days * self.car.daily_price
    
    