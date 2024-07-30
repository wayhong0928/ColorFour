from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

  class Meta:
    model = UserProfile
    fields = ['user', 'line_id', 'is_new_user']
