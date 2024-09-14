from django.db import models
from django.conf import settings

class WeatherConditions(models.Model):
  location = models.CharField(max_length=255)
  temperature = models.DecimalField(max_digits=5, decimal_places=2)
  humidity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  weather_type = models.CharField(max_length=50)
  captured_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'outfit_recommender_weatherconditions'


class OutfitRecommendations(models.Model):
  RECOMMENDATION_TYPE_CHOICES = [
    ('Smart', 'Smart'),
    ('Preference', 'Preference'),
  ]

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  recommendation_name = models.CharField(max_length=100)
  location = models.CharField(max_length=255, blank=True, null=True)
  weather_condition = models.ForeignKey(WeatherConditions, on_delete=models.SET_NULL, null=True, blank=True)
  occasion = models.ForeignKey('wardrobe_manager.WardrobeOccasion', on_delete=models.SET_NULL, null=True, blank=True)
  skin_tone = models.CharField(max_length=50, blank=True, null=True)
  recommendation_type = models.CharField(max_length=20, choices=RECOMMENDATION_TYPE_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'outfit_recommender_outfitrecommendations'


class OutfitRecommendationResults(models.Model):
  recommendation = models.ForeignKey(OutfitRecommendations, on_delete=models.CASCADE)
  outfit = models.ForeignKey('wardrobe_manager.WardrobeOutfit', on_delete=models.CASCADE)
  selected_by_user = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'outfit_recommender_outfitrecommendationresults'
