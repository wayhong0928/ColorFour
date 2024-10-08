from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WardrobeItemViewSet, WardrobeItemCreateView

router = DefaultRouter()
router.register(r'items', WardrobeItemViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 包含所有 ViewSet 的標準路由
    path('items/create/', WardrobeItemCreateView.as_view(), name='wardrobe_item_create'), #新增衣服
]

# URL 前綴：基於 items 註冊的路由，會生成如下的 API 路徑：
# GET /items/ - 獲取所有非垃圾桶中的項目。
# GET /items/{pk}/ - 獲取特定項目的詳細資料。
# GET /items/trash/ - 獲取垃圾桶中的所有項目。
# POST /items/{pk}/move_to_trash/ - 將特定項目移動到垃圾桶。
# POST /items/{pk}/restore/ - 從垃圾桶恢復特定項目。
# DELETE /items/{pk}/delete/ - 永久刪除特定項目。