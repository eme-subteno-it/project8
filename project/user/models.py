""" Inherit AbstractUser to add attributes """
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Create attributes email and subscribed """

    email = models.EmailField(unique=True, max_length=100)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
