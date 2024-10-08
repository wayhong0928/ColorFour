from django.urls import path
from outfit_recommender import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OutfitRecommendationsViewSet, OutfitRecommendationResultsViewSet, WeatherConditionsViewSet

router = DefaultRouter()
router.register(r'recommendations', OutfitRecommendationsViewSet)
router.register(r'recommendation-results', OutfitRecommendationResultsViewSet)
router.register(r'weather-conditions', WeatherConditionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# GET /recommendations/ - 獲取所有穿搭推薦。
# POST /recommendations/recommend/ - 根據天氣條件進行穿搭推薦。
# GET /recommendations/overview/ - 查看所有推薦的總覽。
# GET /recommendation-results/ - 獲取所有穿搭推薦結果。
# GET /recommendation-results/{id}/ - 獲取指定穿搭推薦結果。
# GET /weather-conditions/ - 獲取所有天氣條件。
# GET /weather-conditions/{id}/ - 獲取指定天氣條件。

