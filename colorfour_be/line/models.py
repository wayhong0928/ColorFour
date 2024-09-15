from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class LineBotUserSessions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_step = models.CharField(max_length=50)
    temp_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'linebot_user_sessions'


class LineBotInteractions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message_received = models.TextField()
    bot_response = models.TextField()
    interaction_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'linebot_interactions'


class LineBotNotifications(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50, blank=True, null=True)
    message_content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')

    class Meta:
        db_table = 'linebot_notifications'

