from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model with additional fields like phone number, DOB, etc.
class CustomUser(AbstractUser):
    user_role =  models.CharField(max_length=15, null=True, blank=True)
    email =  models.CharField(max_length=15, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username