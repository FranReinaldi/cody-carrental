import pytest
from django.core.exceptions import ObjectDoesNotExist
from applications.users.models import CustomUser, UserType


@pytest.mark.django_db
def test_create_user():
    user = CustomUser.objects.create_user(email="user@example.com", username="user123", password="password")
    assert user.email == "user@example.com"
    assert user.username == "user123"
    assert user.check_password("password")
    assert user.user_type == 'C'


@pytest.mark.django_db
def test_create_superuser():
    superuser = CustomUser.objects.create_superuser(email="admin@example.com", username="admin", password="adminpass")
    assert superuser.email == "admin@example.com"
    assert superuser.username == "admin"
    assert superuser.check_password("adminpass")
    assert superuser.is_admin
    assert superuser.is_staff
    assert superuser.is_superuser
    assert superuser.user_type == 'S'


@pytest.mark.django_db
def test_user_type():
    user = CustomUser.objects.create_user(email="user@example.com", username="user123", password="password")
    user_type = UserType.objects.filter(user=user).first()
    assert user_type is not None
    assert user_type.type == 'C'


@pytest.mark.django_db
def test_user_type_superuser():
    superuser = CustomUser.objects.create_superuser(email="admin@example.com", username="admin", password="adminpass")
    user_type = UserType.objects.filter(user=superuser).first()
    assert user_type is not None
    assert user_type.type == 'S'


@pytest.mark.django_db
def test_user_type_nonexistent():
    user = CustomUser.objects.create_user(email="user@example.com", username="user123", password="password")
    with pytest.raises(ObjectDoesNotExist):
        user_type = user.user_type
