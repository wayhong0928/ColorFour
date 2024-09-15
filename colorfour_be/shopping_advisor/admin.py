from django.contrib import admin
from .models import (
    ClothingRecognition,
    ClothingComparison,
    RecognitionLogs
)

@admin.register(ClothingRecognition)
class ClothingRecognitionAdmin(admin.ModelAdmin):
    list_display = ('user', 'main_category', 'sub_category', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'main_category', 'sub_category', 'status')
    list_filter = ('status', 'created_at', 'updated_at')

@admin.register(ClothingComparison)
class ClothingComparisonAdmin(admin.ModelAdmin):
    list_display = ('recognition', 'wardrobe_item', 'similarity_score', 'created_at')
    search_fields = ('recognition__main_category', 'wardrobe_item__item_name')
    list_filter = ('created_at',)

@admin.register(RecognitionLogs)
class RecognitionLogsAdmin(admin.ModelAdmin):
    list_display = ('recognition', 'action', 'created_at')
    search_fields = ('recognition__main_category', 'action')
    list_filter = ('action', 'created_at')

