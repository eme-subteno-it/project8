from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
