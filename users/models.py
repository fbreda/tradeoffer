from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cidade = models.CharField(blank=True, max_length=120)
    estado = models.CharField(blank=True, max_length=20)
    telefone = models.CharField(blank=True, max_length=120)
