import pytest

from django.urls import reverse

from applications.cars.models import Manufacturer
from applications.cars.models import Car


# OBJECTS

@pytest.fixture
def car_objects():
    manufacturer_1 = Manufacturer.objects.create(name='Peugeot')
    manufacturer_2 = Manufacturer.objects.create(name='Ford')
    cars = [
        Car.objects.create(manufacturer=manufacturer_1, model='206', year=2000),
        Car.objects.create(manufacturer=manufacturer_1, model='308', year=2013),
        Car.objects.create(manufacturer=manufacturer_2, model='Focus', year=2018),
        Car.objects.create(manufacturer=manufacturer_2, model='Fiesta', year=1999),
    ]
    return cars


# TEST CARS

@pytest.mark.django_db
def test_car_console_view(client, car_objects):

    # Realizar la solicitud a la vista 'console'
    url = reverse('car-console')
    response = client.get(url)

    # Verificar que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200

    # Verificar que algunos datos esten en el contenido de la respuesta
    for car in car_objects:
        assert car.manufacturer.name in response.content.decode('utf-8')
        assert car.model in response.content.decode('utf-8')
        assert str(car.year) in response.content.decode('utf-8')


@pytest.mark.django_db
def test_car_delete_view(client, car_objects):
    selected_car = car_objects[1]

    url = reverse('car_delete', args=[selected_car.pk])
    response = client.post(url)

    assert response.status_code == 302

    with pytest.raises(Car.DoesNotExist):
        Car.objects.get(pk=selected_car.pk)
