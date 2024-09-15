from django.db import models
from django.conf import settings

class OutfitSchedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    outfit = models.ForeignKey('wardrobe_manager.WardrobeOutfit', on_delete=models.CASCADE)
    google_event_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'outfit_scheduler_outfit_schedule'

"""原來生成的資料庫會有以下問題
 UserPreferences 模型中，user 欄位的反向關聯名稱 (userpreferences) 與另一個應用中的 UserPreferences 模型的 user 欄位發生了衝突。Django 無法區分這兩個模型的反向查詢，因為它們都使用了相同的預設名稱。

class UserPreferences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    linebot_notify_time = models.TimeField(blank=True, null=True)
    google_calendar_sync = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_preferences'
"""

"""修改後的資料表"""
class UserPreferences(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='outfit_scheduler_preferences'  # 新增的 related_name
    )
    linebot_notify_time = models.TimeField(blank=True, null=True)
    google_calendar_sync = models.BooleanField(default=True)

    class Meta:
        db_table = 'outfit_scheduler_user_preferences'



"""
解決方法：

你可以為 user 欄位的反向關聯添加 related_name 參數，這樣 Django 就可以區分這兩個模型。

說明：

related_name='outfit_scheduler_preferences'：這個參數告訴 Django，當你從 User 模型進行反向查詢時，應該使用這個名稱，而不是預設的 userpreferences。這樣，你可以在 User 模型中通過 user.outfit_scheduler_preferences 來查詢 UserPreferences。

如果另一個應用中的 UserPreferences 模型也需要進行類似的修改，則需要為它們的 user 欄位設置不同的 related_name，以避免衝突。

"""




class EventLogs(models.Model):
    schedule = models.ForeignKey(OutfitSchedule, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    log_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'outfit_scheduler_event_logs'
