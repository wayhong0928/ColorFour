# colorfour_be/wardrobe_manager/admin.py
from django.contrib import admin
from .models import (
    ClothMainCategory,
    ClothSubCategory,
    ShoeCategory,
    ShoeSubCategory,
    Brand,
    Color,
    Item,
    Occasion,
    ItemOccasion,
    Outfit,
    OutfitItem,
    OutfitOccasion,
)

# 註冊主要服裝類別
@admin.register(ClothMainCategory)
class ClothMainCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# 註冊次要服裝類別
@admin.register(ClothSubCategory)
class ClothSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_category')
    search_fields = ('name',)
    list_filter = ('main_category',)

# 註冊鞋子主要類別
@admin.register(ShoeCategory)
class ShoeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# 註冊鞋子次要類別
@admin.register(ShoeSubCategory)
class ShoeSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shoe_category')
    search_fields = ('name',)
    list_filter = ('shoe_category',)

# 註冊品牌
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# 註冊顏色
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# 註冊服裝單品
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'user', 'price', 'is_in_trash')
    search_fields = ('item_name', 'content')
    list_filter = ('is_in_trash', 'main_category', 'sub_category', 'shoe_category', 'shoe_sub_category', 'brand', 'color')

# 註冊場合
@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'occasion_name')
    search_fields = ('occasion_name',)

# 註冊服裝與場合的關聯
@admin.register(ItemOccasion)
class ItemOccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'occasion')
    list_filter = ('occasion',)

# 註冊穿搭組合
@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit_name', 'user', 'created_at')
    search_fields = ('outfit_name', 'description')

# 註冊穿搭組合的單品
@admin.register(OutfitItem)
class OutfitItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit', 'item')

# 註冊穿搭組合的場合
@admin.register(OutfitOccasion)
class OutfitOccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit', 'occasion')