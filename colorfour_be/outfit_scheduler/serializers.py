from rest_framework import serializers
from .models import (
    OutfitSchedule,
    UserPreferences,
    EventLogs
)

class OutfitScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitSchedule
        fields = "__all__"

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = "__all__"

class EventLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLogs
        fields = "__all__"
