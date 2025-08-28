from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


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


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="posts"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return first 30 characters of content for readability
        return f"{self.author.username}: {self.content[:30]}"
