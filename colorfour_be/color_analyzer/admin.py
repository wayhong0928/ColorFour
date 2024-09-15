from django.contrib import admin
from .models import (
    ColorTestQuestions,
    ColorTestOptions,
    UserColorTests,
    UserColorTestAnswers
)

@admin.register(ColorTestQuestions)
class ColorTestQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'requires_user_image', 'created_at')
    search_fields = ('question_text',)
    list_filter = ('requires_user_image', 'created_at')

@admin.register(ColorTestOptions)
class ColorTestOptionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_text', 'color_code', 'created_at')
    search_fields = ('option_text', 'color_code')
    list_filter = ('created_at',)

@admin.register(UserColorTests)
class UserColorTestsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'result_type', 'started_at', 'completed_at')
    search_fields = ('user__username', 'title', 'result_type')
    list_filter = ('result_type', 'started_at', 'completed_at')

@admin.register(UserColorTestAnswers)
class UserColorTestAnswersAdmin(admin.ModelAdmin):
    list_display = ('test', 'question', 'selected_option', 'answered_at')
    search_fields = ('test__title', 'question__question_text', 'selected_option__option_text')
    list_filter = ('answered_at',)

