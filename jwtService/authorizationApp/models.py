from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    scope = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username