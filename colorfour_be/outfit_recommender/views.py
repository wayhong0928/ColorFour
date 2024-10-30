import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import (
    WeatherConditions,
    OutfitRecommendations,
    OutfitRecommendationResults,
)
from .serializers import (
    WeatherConditionsSerializer,
    OutfitRecommendationsSerializer,
    OutfitRecommendationResultsSerializer,
)


class OutfitRecommendationsViewSet(viewsets.ModelViewSet):
    queryset = OutfitRecommendations.objects.all()
    serializer_class = OutfitRecommendationsSerializer

    @action(detail=False, methods=["post"])
    def recommend(self, request):
        try:
            data = request.data
            data["user"] = request.user.username  # 儲存使用者名稱

            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            traceback.print_exc()
            return Response({"error": "內部伺服器錯誤"}, status=500)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


class OutfitRecommendationResultsViewSet(viewsets.ModelViewSet):
    queryset = OutfitRecommendationResults.objects.all()
    serializer_class = OutfitRecommendationResultsSerializer

    def get_queryset(self):
        user = self.request.user.get_username()
        return self.queryset.filter(recommendation__icontains=user)  # 使用名稱進行篩選


class WeatherConditionsViewSet(viewsets.ModelViewSet):
    queryset = WeatherConditions.objects.all()
    serializer_class = WeatherConditionsSerializer
