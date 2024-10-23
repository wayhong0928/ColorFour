from django.db import models
from django.conf import settings

class ColorTestQuestions(models.Model):
    question_text = models.CharField(max_length=255)
    requires_user_image = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'color_analyzer_color_test_questions'


class ColorTestOptions(models.Model):
    question = models.ForeignKey(ColorTestQuestions, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    color_code = models.CharField(max_length=7)  # 如 "#FFFFFF" 這類的色碼
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'color_analyzer_color_test_options'


class UserColorTests(models.Model):
    RESULT_TYPE_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Winter', 'Winter'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_image_url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    result_type = models.CharField(max_length=10, choices=RESULT_TYPE_CHOICES)

    class Meta:
        db_table = 'color_analyzer_user_color_tests'


class UserColorTestAnswers(models.Model):
    test = models.ForeignKey(UserColorTests, on_delete=models.CASCADE)
    question = models.ForeignKey(ColorTestQuestions, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(ColorTestOptions, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'color_analyzer_user_color_test_answers'

