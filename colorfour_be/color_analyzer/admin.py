from django.contrib import admin
from django.utils.html import format_html
from .models import UserColorTest


@admin.register(UserColorTest)
class UserColorTestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "test_name",
        "result_type",
        "test_date",
        "uploaded_image_preview",
    )
    list_filter = ("result_type", "test_date")
    search_fields = ("user__username",)
    readonly_fields = ("test_date",)

    def uploaded_image_preview(self, obj):
        """顯示上傳的圖片預覽"""
        if obj.uploaded_image:
            return format_html(
                '<img src="{}" style="max-height: 400px;"/>', obj.uploaded_image.url
            )
        return "無圖片"

    uploaded_image_preview.short_description = "圖片預覽"
