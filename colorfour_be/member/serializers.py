from rest_framework import serializers
from .models import (
    User,
    Role,
    SubscriptionPlan,
    UserPreferences,
    UserInteractionHistory,
    UserAuthProvider,
)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "role_name"]


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ["id", "plan_name", "price", "features"]


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = [
            "id",
            "user",
            "preferred_language",
            "theme",
            "notification_linebot",
            "preferred_outfit_recommendation",
        ]


class UserInteractionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteractionHistory
        fields = [
            "id",
            "user",
            "actions",
            "target_id",
            "target_type",
            "timestamp",
            "details",
        ]


class UserAuthProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthProvider
        fields = ["id", "user", "provider", "provider_id", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    subscription_plan = SubscriptionPlanSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "profile_picture",
            "role",
            "subscription_plan",
            "date_joined",
            "last_login",
            "updated_at",
            "is_active",
        ]
