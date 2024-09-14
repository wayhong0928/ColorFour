from django.contrib import admin
from .models import (
    OutfitSchedule,
    UserPreferences,
    EventLogs
)

@admin.register(OutfitSchedule)
class OutfitScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule_name', 'start_time', 'end_time', 'location', 'created_at', 'updated_at')
    search_fields = ('user__username', 'schedule_name', 'location')
    list_filter = ('start_time', 'end_time')

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'linebot_notify_time', 'google_calendar_sync')
    search_fields = ('user__username',)

@admin.register(EventLogs)
class EventLogsAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'action', 'created_at')
    search_fields = ('schedule__schedule_name', 'action')
    list_filter = ('action', 'created_at')
