from django.urls import path
from .views import WardrobeItemListCreate, WardrobeItemListInGarbage, WardrobeItemDetail, DeleteFromGarbage

urlpatterns = [
    path('items/', WardrobeItemListCreate.as_view(), name='wardrobe_list_create'),
    path('items/garbage', WardrobeItemListInGarbage.as_view(), name='wardrobe_list_create'),
    path('items/<int:pk>/', WardrobeItemDetail.as_view(), name='wardrobe_detail_update_delete'),
    path('items/<int:item_id>/delete/', DeleteFromGarbage.as_view(), name='wardrobe_delete_permanently'),
]
