from rest_framework import serializers
from .models import LineBotUserSessions, LineBotInteractions, LineBotNotifications


class LineBotUserSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineBotUserSessions
        fields = "__all__"


class LineBotInteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineBotInteractions
        fields = "__all__"


class LineBotNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineBotNotifications
        fields = "__all__"
