from django.contrib import admin
from django.urls import path, include
from .views import console, new_manufacturer, new_car, car_delete, car_detail

urlpatterns = [
    path('console/',console, name='car-console'),
    path('new-brand/',new_manufacturer , name='new_brand'),
    path('new-car/',new_car , name='new_car'),
    path('<int:pk>/delete/', car_delete, name='car_delete'),
    path('<int:car_id>/',car_detail, name='car_detail'),

]