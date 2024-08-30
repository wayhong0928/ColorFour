from django.contrib import admin
from .models import (
    WardrobeCategory,
    WardrobeType,
    WardrobeItem,
    WardrobeOccasion,
    WardrobeItemOccasion,
    WardrobeOutfit,
    WardrobeOutfitItem,
    WardrobeOutfitOccasion,
)

# 註冊 WardrobeCategory 模型到 Django 管理後台
@admin.register(WardrobeCategory)
class WardrobeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)

# 註冊 WardrobeType 模型到 Django 管理後台
@admin.register(WardrobeType)
class WardrobeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'type_name', 'temperature')
    search_fields = ('type_name',)
    list_filter = ('category',)

# 註冊 WardrobeItem 模型到 Django 管理後台
@admin.register(WardrobeItem)
class WardrobeItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'item_name', 'brand', 'color', 'price', 'is_in_trash', 'created_at', 'latest_edit')
    search_fields = ('item_name', 'brand', 'color')
    list_filter = ('type', 'is_in_trash', 'brand', 'color')
    date_hierarchy = 'created_at'

# 註冊 WardrobeOccasion 模型到 Django 管理後台
@admin.register(WardrobeOccasion)
class WardrobeOccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'occasion_name')
    search_fields = ('occasion_name',)

# 註冊 WardrobeItemOccasion 模型到 Django 管理後台
@admin.register(WardrobeItemOccasion)
class WardrobeItemOccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'occasion')
    search_fields = ('item__item_name', 'occasion__occasion_name')
    list_filter = ('occasion',)

# 註冊 WardrobeOutfit 模型到 Django 管理後台
@admin.register(WardrobeOutfit)
class WardrobeOutfitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'outfit_name', 'description', 'created_at', 'latest_edit')
    search_fields = ('outfit_name', 'description')
    list_filter = ('user',)
    date_hierarchy = 'created_at'

# 註冊 WardrobeOutfitItem 模型到 Django 管理後台
@admin.register(WardrobeOutfitItem)
class WardrobeOutfitItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit', 'item')
    search_fields = ('outfit__outfit_name', 'item__item_name')
    list_filter = ('outfit',)

# 註冊 WardrobeOutfitOccasion 模型到 Django 管理後台
@admin.register(WardrobeOutfitOccasion)
class WardrobeOutfitOccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'outfit', 'occasion')
    search_fields = ('outfit__outfit_name', 'occasion__occasion_name')
    list_filter = ('occasion',)
