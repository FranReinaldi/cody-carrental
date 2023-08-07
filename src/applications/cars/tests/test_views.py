import pytest

from django.test import Client
from django.urls import reverse

from applications.cars.models import Manufacturer
from applications.cars.models import Car


@pytest.mark.django_db
def test_console_view():
    client = Client()

    # Crear algunos autos de ejemplo en la base de datos
    manufacturer = Manufacturer.objects.create(name='Peugeot')

    Car.objects.create(
        manufacturer=manufacturer,
        model='206',
        year=2000
    )
    Car.objects.create(
        manufacturer=manufacturer,
        model='308',
        year=2013
    )

    # Realizar la solicitud a la vista 'console'
    url = reverse('car-console')
    response = client.get(url)

    # Verificar que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200

    # Verificar que algunos datos esten en el contenido de la respuesta
    assert "206" in response.content.decode('utf-8')
    assert "Peugeot" in response.content.decode('utf-8')
