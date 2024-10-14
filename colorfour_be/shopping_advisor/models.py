from django.db import models
from django.conf import settings

class ClothingRecognition(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    main_category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.CharField(max_length=255)
    processed_image_url = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    similarity_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    suitability_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shopping_advisor_clothing_recognition'


class ClothingComparison(models.Model):
    recognition = models.ForeignKey(ClothingRecognition, on_delete=models.CASCADE)
    wardrobe_item = models.ForeignKey('wardrobe_manager.Item', on_delete=models.CASCADE)
    similarity_score = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shopping_advisor_clothing_comparison'


class RecognitionLogs(models.Model):
    recognition = models.ForeignKey(ClothingRecognition, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    log_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shopping_advisor_recognition_logs'

