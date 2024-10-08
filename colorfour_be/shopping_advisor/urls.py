from django.urls import path, include
from shopping_advisor import views


from rest_framework.routers import DefaultRouter
from .views import ClothingRecognitionViewSet, ClothingComparisonViewSet

router = DefaultRouter()
router.register(r'recognitions', ClothingRecognitionViewSet)
router.register(r'comparisons', ClothingComparisonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# GET /recognitions/ - 獲取所有衣物識別記錄。
# POST /recognitions/recommend/ - 基於衣物識別進行推薦。
# GET /recognitions/overview/ - 查看所有衣物識別的推薦總覽。
# GET /comparisons/ - 獲取所有衣物比較記錄。
# GET /comparisons/{id}/ - 獲取指定衣物比較記錄。