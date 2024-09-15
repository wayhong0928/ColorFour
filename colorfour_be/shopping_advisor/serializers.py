from rest_framework import serializers
from .models import (
    ClothingRecognition,
    ClothingComparison,
    RecognitionLogs
)

class ClothingRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingRecognition
        fields = "__all__"

class ClothingComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingComparison
        fields = "__all__"

class RecognitionLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionLogs
        fields = "__all__"
