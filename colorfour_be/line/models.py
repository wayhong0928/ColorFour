from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoogleOAuthToken(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  access_token = models.CharField(max_length=255)
  refresh_token = models.CharField(max_length=255, blank=True, null=True)
  expires_at = models.DateTimeField()

  def __str__(self):
    return f"{self.user.username}'s Google OAuth Token"
