import traceback
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


from wardrobe_manager.models import Occasion
from .models import WeatherConditions, OutfitRecommendations, OutfitRecommendationResults
from .serializers import (
    WeatherConditionsSerializer,
    OutfitRecommendationsSerializer,
    OutfitRecommendationResultsSerializer
)


class OutfitRecommendationsViewSet(viewsets.ModelViewSet):
    queryset = OutfitRecommendations.objects.all()
    serializer_class = OutfitRecommendationsSerializer
    permission_classes = [IsAuthenticated]  # 驗證使用者已登入

    @action(detail=False, methods=['post'])
    def recommend(self, request):
        try:
            data = request.data
            print("收到的資料:", data)  # 偵錯

            # 根據 occasion_name 查找 Occasion 對象
            occasion_name = data.get('occasion')
            if occasion_name:
                try:
                    occasion_obj = Occasion.objects.get(occasion_name=occasion_name)
                    data['occasion'] = occasion_obj.id  # 替換為 ID
                except Occasion.DoesNotExist:
                    return Response({"error": "無效的場合名稱"}, status=400)

            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                # 保存推薦資料與當前使用者的關聯
                serializer.save(user=request.user)
                return Response(serializer.data, status=201)
            else:
                print("序列化器錯誤:", serializer.errors)  # 偵錯
                return Response(serializer.errors, status=400)

        except Exception as e:
            print(f"未預期的錯誤: {e}")
            traceback.print_exc()  # 列出錯誤追蹤
            return Response({"error": "內部伺服器錯誤"}, status=500)




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
