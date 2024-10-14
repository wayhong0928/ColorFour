from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import WeatherConditions, OutfitRecommendations, OutfitRecommendationResults
from .serializers import (
    WeatherConditionsSerializer,
    OutfitRecommendationsSerializer,
    OutfitRecommendationResultsSerializer
)

class OutfitRecommendationsViewSet(viewsets.ModelViewSet):
  queryset = OutfitRecommendations.objects.all()
  serializer_class = OutfitRecommendationsSerializer

  @action(detail=False, methods=['post'])
  def recommend(self, request):
    """進行推薦"""
    # 假設使用氣象條件進行推薦，請根據需求調整推薦邏輯
    weather_condition_id = request.data.get('weather_condition_id')
    try:
      weather_condition = WeatherConditions.objects.get(id=weather_condition_id)
      # 假設根據氣象條件進行推薦邏輯，這裡可以進行更複雜的推薦計算
      recommended_outfits = OutfitRecommendations.objects.filter(weather_condition=weather_condition)
      serializer = self.get_serializer(recommended_outfits, many=True)
      return Response(serializer.data)
    except WeatherConditions.DoesNotExist:
      return Response({"error": "Weather condition not found"}, status=404)

  @action(detail=False, methods=['get'])
  def overview(self, request):
    """顯示推薦總覽"""
    recommendations = self.get_queryset()
    serializer = self.get_serializer(recommendations, many=True)
    return Response(serializer.data)

class OutfitRecommendationResultsViewSet(viewsets.ModelViewSet):
  queryset = OutfitRecommendationResults.objects.all()
  serializer_class = OutfitRecommendationResultsSerializer

  def retrieve(self, request, *args, **kwargs):
    """顯示推薦結果頁面"""
    recommendation_result = self.get_object()
    serializer = self.get_serializer(recommendation_result)
    return Response(serializer.data)

class WeatherConditionsViewSet(viewsets.ModelViewSet):
  queryset = WeatherConditions.objects.all()
  serializer_class = WeatherConditionsSerializer
