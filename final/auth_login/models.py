from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class SuperAdmin(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)


class Guest(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
