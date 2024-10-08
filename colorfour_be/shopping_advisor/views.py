from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ClothingRecognition, ClothingComparison
from .serializers import ClothingRecognitionSerializer, ClothingComparisonSerializer

class ClothingRecognitionViewSet(viewsets.ModelViewSet):
  queryset = ClothingRecognition.objects.all()
  serializer_class = ClothingRecognitionSerializer

  @action(detail=False, methods=['post'])
  def recommend(self, request):
    """進行推薦"""
    # 假設進行推薦時需要基於識別的衣物，請根據需求進行具體推薦邏輯
    recognition_id = request.data.get('recognition_id')
    try:
      recognition = ClothingRecognition.objects.get(id=recognition_id)
      # 基於識別的衣物進行推薦計算，這裡可以進行具體的比較邏輯
      comparison_results = ClothingComparison.objects.filter(recognition=recognition)
      serializer = ClothingComparisonSerializer(comparison_results, many=True)
      return Response(serializer.data)
    except ClothingRecognition.DoesNotExist:
      return Response({"error": "Clothing recognition not found"}, status=404)

  @action(detail=False, methods=['get'])
  def overview(self, request):
    """推薦總覽"""
    recognitions = self.get_queryset()
    serializer = self.get_serializer(recognitions, many=True)
    return Response(serializer.data)

class ClothingComparisonViewSet(viewsets.ModelViewSet):
  queryset = ClothingComparison.objects.all()
  serializer_class = ClothingComparisonSerializer
