import pytest
from datetime import date

from applications.users.models import CustomUser

from applications.cars.models import Manufacturer, Car, Rental



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


@pytest.fixture
def sample_user():
    return CustomUser.objects.create(username='testuser')


@pytest.fixture
def sample_rental(example_car, sample_user):
    return Rental.objects.create(
        car=example_car,
        start_date=date(2023, 8, 1),
        end_date=date(2023, 8, 5),
        calification=4,
        customer=sample_user
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


#TEST RENTAL

@pytest.mark.django_db
def test_rental_creation(sample_rental):
    assert sample_rental.id is not None


@pytest.mark.django_db
def test_rental_car_relationship(sample_rental, example_car):
    assert sample_rental.car == example_car


@pytest.mark.django_db
def test_rental_customer_relationship(sample_rental, sample_user):
    assert sample_rental.customer == sample_user


@pytest.mark.django_db
def test_rental_dates(sample_rental):
    assert sample_rental.start_date <= sample_rental.end_date


@pytest.mark.django_db
def test_rental_calification(sample_rental):
    assert 1 <= sample_rental.calification <= 5
