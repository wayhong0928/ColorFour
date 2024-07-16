from django.urls import path, include
from django.contrib import admin
from wardrobe_manager import views
from .views import add_wardrobe_item

# 測試API *
from .views import WardrobeItemListCreate


urlpatterns = [
	path('add/', add_wardrobe_item, name="add_wardrobe_item"),  # add衣服

	# 測試API *
	path('api/items/', WardrobeItemListCreate.as_view(), name='wardrobeitem-list-create'),  # 新增 API 路由
]
