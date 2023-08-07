import pytest
from applications.cars.models import Manufacturer
from applications.cars.models import Car


# CREACION DE OBJETOS

@pytest.fixture
def example_manufacturer():
    return Manufacturer.objects.create(name='Peugeot')


@pytest.fixture
def example_car(example_manufacturer):
    return Car.objects.create(
        manufacturer=example_manufacturer,
        model='308',
        year=2013,
    )


# TEST MANUFACTUTER

@pytest.mark.django_db
def test_manufacturer_name(example_manufacturer):
    assert example_manufacturer.name == 'Peugeot'


# TEST CAR

@pytest.mark.django_db
def test_car_manufacturer(example_car):
    assert example_car.manufacturer.name == 'Peugeot'


@pytest.mark.django_db
def test_car_model(example_car):
    assert example_car.model == '308'


@pytest.mark.django_db
def test_car_year(example_car):
    assert example_car.year == 2013
