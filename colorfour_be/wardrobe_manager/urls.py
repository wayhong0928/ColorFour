from django.urls import path, include
from django.contrib import admin
from wardrobe_manager import views
from .views import add_wardrobe_item, DeleteWardrobeItemView, UpdateWardrobeItemView

# 測試API *
from .views import WardrobeItemListCreate


urlpatterns = [
    path('add/', add_wardrobe_item, name="add_wardrobe_item"),  # add衣服
    path('delete/<int:item_id>/', DeleteWardrobeItemView.as_view(), name='delete_item'), #delete衣服
    path('update/<int:item_id>/', UpdateWardrobeItemView.as_view(), name='update_item'), #update衣服
    
    # 測試API *
    path('api/items/', WardrobeItemListCreate.as_view(), name='wardrobeitem-list-create'),  # 新增 API 路由
]
