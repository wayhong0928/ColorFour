from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OutfitRecommendationsViewSet,
    OutfitRecommendationResultsViewSet,
    WeatherConditionsViewSet,
)

router = DefaultRouter()
router.register(r"recommendations", OutfitRecommendationsViewSet)
router.register(r"recommendation-results", OutfitRecommendationResultsViewSet)
router.register(r"weather-conditions", WeatherConditionsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

# Recommendations API (穿搭推薦相關)
# GET  /recommendations/               - 獲取所有穿搭推薦。
# POST /recommendations/               - 新增一筆穿搭推薦。
# POST /recommendations/recommend/     - 根據天氣條件進行穿搭推薦。
# GET  /recommendations/{id}/          - 獲取指定的穿搭推薦資料。
# PUT  /recommendations/{id}/          - 更新指定的穿搭推薦資料。
# PATCH /recommendations/{id}/         - 部分更新指定的穿搭推薦資料。
# DELETE /recommendations/{id}/        - 刪除指定的穿搭推薦資料。

# Recommendation Results API (推薦結果相關)
# GET  /recommendation-results/        - 獲取所有穿搭推薦結果。
# POST /recommendation-results/        - 新增穿搭推薦結果。
# GET  /recommendation-results/{id}/   - 獲取指定的穿搭推薦結果。
# PUT  /recommendation-results/{id}/   - 更新指定的推薦結果資料。
# PATCH /recommendation-results/{id}/  - 部分更新指定的推薦結果資料。
# DELETE /recommendation-results/{id}/ - 刪除指定的推薦結果資料。

# Weather Conditions API (天氣條件相關)
# GET  /weather-conditions/            - 獲取所有天氣條件。
# POST /weather-conditions/            - 新增一筆天氣條件資料。
# GET  /weather-conditions/{id}/       - 獲取指定的天氣條件資料。
# PUT  /weather-conditions/{id}/       - 更新指定的天氣條件資料。
# PATCH /weather-conditions/{id}/      - 部分更新指定的天氣條件資料。
# DELETE /weather-conditions/{id}/     - 刪除指定的天氣條件資料。
