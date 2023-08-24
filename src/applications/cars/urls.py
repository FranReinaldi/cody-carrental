from django.contrib import admin
from django.urls import path, include
from .views import (console, new_manufacturer, new_car, 
                    car_delete, car_detail, brand_detail,
                    brand_delete, rental_console,new_rental,
                    rental_detail, cars_export_pdf, rental_calification)

urlpatterns = [
    path('console/',console, name='car-console'),
    path('new-brand/',new_manufacturer , name='new_brand'),
    path('new-car/',new_car , name='new_car'),
    path('<int:pk>/delete/', car_delete, name='car_delete'),
    path('<int:car_id>/',car_detail, name='car_detail'),
    path('brand/<int:brand_id>/',brand_detail, name='brand_detail'),
    path('brand/<int:pk>/delete',brand_delete, name='brand_delete'),
    path('rentals/',rental_console, name='rental-console'),
    path('new-rental/',new_rental, name='new_rental'),
    path('rental/<int:rental_id>/',rental_detail, name='rental_detail'),
    path('rental/<int:rental_id>/calification',rental_calification, name='rental_calification'),

    # EXPORT PDF
    path('console/export_pdf', cars_export_pdf, name='cars_export_pdf'),
    

]