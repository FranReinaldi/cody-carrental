from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .functions import create_user


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = create_user(self, email, username, password)
        user_type = UserType.objects.create(user=user,type='C')
        return user

    def create_superuser(self, email, username, password=None):
        user = create_user(self, email, username, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        user_type = UserType.objects.create(user=user,type='S')
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property    
    def user_type(self):
        return UserType.objects.filter(user=self).first().type


class UserType(models.Model):

    TYPE_CHOICES = (
        ('S','STAFF'),
        ('C','CLIENT')
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, default='C', max_length=2)
