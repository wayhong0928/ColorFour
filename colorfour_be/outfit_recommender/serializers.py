from rest_framework import serializers
from .models import (
    WeatherConditions,
    OutfitRecommendations,
    OutfitRecommendationResults,
)


class WeatherConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherConditions
        fields = "__all__"


class OutfitRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendations
        fields = [
            "id",
            "recommendation_name",
            "recommendation_image",
            "location",
            "occasion",
            "skin_tone",
            "created_at",
        ]
        extra_kwargs = {"created_at": {"read_only": True}}


class OutfitRecommendationResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendationResults
        fields = "__all__"
