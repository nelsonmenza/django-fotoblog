from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLES_CHOICES = ((CREATOR, 'Creator'), (SUBSCRIBER, 'Subscriber'))

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLES_CHOICES)
