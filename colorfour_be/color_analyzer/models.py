from django.db import models
from django.conf import settings

class UserColorTest(models.Model):
    RESULT_TYPE_CHOICES = [
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Autumn", "Autumn"),
        ("Winter", "Winter"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)         # 關聯用戶
    test_name = models.CharField(max_length=50, default="未命名測驗")                     # 測驗名稱
    uploaded_image = models.ImageField(upload_to="color_tests/", blank=True, null=True)  # 上傳圖片
    result_type = models.CharField(max_length=10, choices=RESULT_TYPE_CHOICES)           # 測試結果
    test_date = models.DateTimeField(auto_now_add=True)                                  # 測試日期

    class Meta:
        db_table = "user_color_tests"
        ordering = ['-test_date']  # 預設按測試日期降序排列
