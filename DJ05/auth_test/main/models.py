# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     phone_number = models.CharField("Номер телефона", max_length=15, unique=True)
#     email = models.EmailField("Электронная почта", unique=True)
#
#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField("Номер телефона", max_length=15, unique=False, blank=True, null=True)
    email = models.EmailField("Электронная почта", unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
