from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('verified', 'Verified User'),
        ('regular', 'Regular User'),
    )

    # extra fields
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    bio = models.TextField(blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
