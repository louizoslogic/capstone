from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    summonername = models.CharField(max_length=30)
    region = models.CharField(max_length=10)
    accountId = models.CharField(max_length=300, null=True)
    puuid = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.username
