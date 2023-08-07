import pytest
from applications.cars.models import Manufacturer

@pytest.fixture
def example_manufacturer():
    return Manufacturer.objects.create(name='Peugeot')

@pytest.mark.django_db
def test_manufacturer_name(example_manufacturer):
    assert example_manufacturer.name == 'Peugeot'