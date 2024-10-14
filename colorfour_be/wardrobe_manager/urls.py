# colorfour_be/wardrobe_manager/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ClothCategoryViewSet, ClothSubCategoryViewSet, ItemViewSet, OccasionViewSet, ItemOccasionViewSet, OutfitViewSet, OutfitItemViewSet, OutfitOccasionViewSet, ShoeCategoryViewSet, ShoeSubCategoryViewSet, BrandViewSet, ColorViewSet)

router = DefaultRouter()
router.register(r'categories', ClothCategoryViewSet)  # 主要服裝類別
router.register(r'subcategories', ClothSubCategoryViewSet)   # 次要服裝類別
router.register(r'items', ItemViewSet)           # 服裝單品
router.register(r'brands', BrandViewSet)         # 品牌
router.register(r'colors', ColorViewSet)         # 顏色
router.register(r'occasions', OccasionViewSet)   # 場合
router.register(r'item_occasions', ItemOccasionViewSet)  # 服裝與場合的關聯
router.register(r'outfits', OutfitViewSet)       # 穿搭組合
router.register(r'outfit_items', OutfitItemViewSet)  # 穿搭組合的單品
router.register(r'outfit_occasions', OutfitOccasionViewSet)  # 穿搭組合的場合
router.register(r'shoes_categories', ShoeCategoryViewSet)  # 鞋子主要類別
router.register(r'shoes_subcategories', ShoeSubCategoryViewSet)  # 鞋子次要類別

urlpatterns = [
    path('', include(router.urls)),  
]

# API 路徑說明
# 主要服裝類別
# GET /categories/ - 獲取所有主要服裝類別
# POST /categories/ - 創建新的主要服裝類別
# GET /categories/{id}/ - 獲取指定 ID 的主要服裝類別
# PUT /categories/{id}/ - 更新指定 ID 的主要服裝類別
# DELETE /categories/{id}/ - 刪除指定 ID 的主要服裝類別

# 次要服裝類別
# GET /subcategories/ - 獲取所有次要服裝類別
# POST /subcategories/ - 創建新的次要服裝類別
# GET /subcategories/{id}/ - 獲取指定 ID 的次要服裝類別
# PUT /subcategories/{id}/ - 更新指定 ID 的次要服裝類別
# DELETE /subcategories/{id}/ - 刪除指定 ID 的次要服裝類別

# 服裝單品
# GET /items/ - 獲取所有服裝單品
# POST /items/ - 創建新的服裝單品
# GET /items/{id}/ - 獲取指定 ID 的服裝單品
# PUT /items/{id}/ - 更新指定 ID 的服裝單品
# DELETE /items/{id}/ - 刪除指定 ID 的服裝單品

# 場合
# GET /occasions/ - 獲取所有場合
# POST /occasions/ - 創建新的場合
# GET /occasions/{id}/ - 獲取指定 ID 的場合
# PUT /occasions/{id}/ - 更新指定 ID 的場合
# DELETE /occasions/{id}/ - 刪除指定 ID 的場合

# 服裝與場合的關聯
# GET /item_occasions/ - 獲取所有服裝與場合的關聯
# POST /item_occasions/ - 創建新的服裝與場合的關聯
# GET /item_occasions/{id}/ - 獲取指定 ID 的關聯
# PUT /item_occasions/{id}/ - 更新指定 ID 的關聯
# DELETE /item_occasions/{id}/ - 刪除指定 ID 的關聯

# 穿搭組合
# GET /outfits/ - 獲取所有穿搭組合
# POST /outfits/ - 創建新的穿搭組合
# GET /outfits/{id}/ - 獲取指定 ID 的穿搭組合
# PUT /outfits/{id}/ - 更新指定 ID 的穿搭組合
# DELETE /outfits/{id}/ - 刪除指定 ID 的穿搭組合

# 穿搭組合的單品
# GET /outfit_items/ - 獲取所有穿搭組合的單品
# POST /outfit_items/ - 創建新的穿搭組合的單品
# GET /outfit_items/{id}/ - 獲取指定 ID 的穿搭組合的單品
# PUT /outfit_items/{id}/ - 更新指定 ID 的穿搭組合的單品
# DELETE /outfit_items/{id}/ - 刪除指定 ID 的穿搭組合的單品

# 穿搭組合的場合
# GET /outfit_occasions/ - 獲取所有穿搭組合的場合
# POST /outfit_occasions/ - 創建新的穿搭組合的場合
# GET /outfit_occasions/{id}/ - 獲取指定 ID 的穿搭組合的場合
# PUT /outfit_occasions/{id}/ - 更新指定 ID 的穿搭組合的場合
# DELETE /outfit_occasions/{id}/ - 刪除指定 ID 的穿搭組合的場合

# 鞋子主要類別
# GET /shoes_categories/ - 獲取所有鞋子主要類別
# POST /shoes_categories/ - 創建新的鞋子主要類別
# GET /shoes_categories/{id}/ - 獲取指定 ID 的鞋子主要類別
# PUT /shoes_categories/{id}/ - 更新指定 ID 的鞋子主要類別
# DELETE /shoes_categories/{id}/ - 刪除指定 ID 的鞋子主要類別

# 鞋子次要類別
# GET /shoes_types/ - 獲取所有鞋子次要類別
# POST /shoes_types/ - 創建新的鞋子次要類別
# GET /shoes_types/{id}/ - 獲取指定 ID 的鞋子次要類別
# PUT /shoes_types/{id}/ - 更新指定 ID 的鞋子次要類別
# DELETE /shoes_types/{id}/ - 刪除指定 ID 的鞋子次要類別