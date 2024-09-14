from django.contrib import admin
from .models import (
    LineBotUserSessions,
    LineBotInteractions,
    LineBotNotifications
)

@admin.register(LineBotUserSessions)
class LineBotUserSessionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_step', 'created_at', 'updated_at')
    search_fields = ('user__username', 'current_step')

@admin.register(LineBotInteractions)
class LineBotInteractionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'interaction_time')
    search_fields = ('user__username', 'message_received', 'bot_response')
    list_filter = ('interaction_time',)

@admin.register(LineBotNotifications)
class LineBotNotificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'status', 'send_time')
    search_fields = ('user__username', 'notification_type', 'message_content')
    list_filter = ('status', 'send_time')

