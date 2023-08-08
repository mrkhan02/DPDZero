from typing import Tuple
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("The username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username,email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username,email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    full_name=models.CharField(max_length=100,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','full_name','age','gender']

    def __str__(self):
        return self.username


class Item(models.Model):
    key = models.CharField(max_length=100,unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key