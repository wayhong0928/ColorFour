from rest_framework import serializers
from .models import (
    WeatherConditions,
    OutfitRecommendations,
    OutfitRecommendationResults
)

class WeatherConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherConditions
        fields = "__all__"

class OutfitRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendations
        fields = "__all__"

class OutfitRecommendationResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendationResults
        fields = "__all__"
