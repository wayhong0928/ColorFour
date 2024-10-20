from rest_framework import serializers
from wardrobe_manager.models import Occasion
from .models import (
    WeatherConditions,
    OutfitRecommendations,
    OutfitRecommendationResults,
)

class WeatherConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherConditions
        fields = "__all__"

class OutfitRecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendations
        fields = ['recommendation_name', 'location', 'occasion', 'skin_tone', 'created_at']
        extra_kwargs = {
            'occasion': {'required': False, 'allow_null': True},
            'skin_tone': {'required': False, 'allow_null': True},
            'created_at': {'read_only': True},
            'user': {'required': False}
        }

    def validate(self, data):
        # 確認 recommendation_name 是否存在且不為空
        if not data.get('recommendation_name'):
            raise serializers.ValidationError({"recommendation_name": "此欄位不可為空白。"})

        # 確保 occasion 是有效的 ForeignKey ID
        occasion_name = data.get('occasion')
        if occasion_name:
            try:
                occasion_obj = Occasion.objects.get(name=occasion_name)
                data['occasion'] = occasion_obj  # 將字串轉為對應的模型實例
            except Occasion.DoesNotExist:
                raise serializers.ValidationError({"occasion": "無效的場合名稱。"})

        return data

    def create(self, validated_data):
        return super().create(validated_data)


class OutfitRecommendationResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitRecommendationResults
        fields = "__all__"
