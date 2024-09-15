from django.contrib import admin
from .models import (
    WeatherConditions,
    OutfitRecommendations,
    OutfitRecommendationResults
)

@admin.register(WeatherConditions)
class WeatherConditionsAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'humidity', 'weather_type', 'captured_at')
    search_fields = ('location', 'weather_type')
    list_filter = ('weather_type', 'captured_at')

@admin.register(OutfitRecommendations)
class OutfitRecommendationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommendation_name', 'location', 'skin_tone', 'recommendation_type', 'created_at')
    search_fields = ('recommendation_name', 'location', 'skin_tone')
    list_filter = ('recommendation_type', 'created_at')

@admin.register(OutfitRecommendationResults)
class OutfitRecommendationResultsAdmin(admin.ModelAdmin):
    list_display = ('recommendation', 'outfit', 'selected_by_user', 'created_at')
    search_fields = ('recommendation__recommendation_name', 'outfit__outfit_name')
    list_filter = ('selected_by_user', 'created_at')

