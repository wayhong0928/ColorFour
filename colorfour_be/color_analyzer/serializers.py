from rest_framework import serializers
from .models import (
    ColorTestQuestions,
    ColorTestOptions,
    UserColorTests,
    UserColorTestAnswers
)

class ColorTestQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorTestQuestions
        fields = "__all__"

class ColorTestOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorTestOptions
        fields = "__all__"

class UserColorTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserColorTests
        fields = "__all__"

class UserColorTestAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserColorTestAnswers
        fields = "__all__"
