from django.db import models
from django.conf import settings


class WeatherConditions(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    weather_type = models.CharField(max_length=50)
    captured_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "outfit_recommender_weatherconditions"


class OutfitRecommendations(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recommendation_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)
    weather_condition = models.JSONField(blank=True, null=True)  # 暫時以 JSON 格式儲存
    occasion = models.CharField(max_length=100, blank=True, null=True)  # 場合名稱暫存為字串
    skin_tone = models.CharField(max_length=50, blank=True, null=True)  # 色彩分析結果暫存為字串
    closet_want = models.CharField(max_length=50, blank=True, null=True)  # 想要穿搭風格暫存為字串
    closet_not_want = models.CharField(max_length=50, blank=True, null=True)  # 不想要穿搭風格暫存為字串
    recommendation_image = models.CharField(max_length=500, null=True, blank=True)
    recommendation_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "outfit_recommender_outfitrecommendations"


class OutfitRecommendationResults(models.Model):
    recommendation = models.CharField(max_length=100)  # 推薦名稱暫存為字串
    outfit = models.JSONField()  # 暫時以 JSON 格式儲存穿搭資料
    selected_by_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "outfit_recommender_outfitrecommendationresults"


"""
class OutfitRecommendations(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  weather_condition = models.ForeignKey(WeatherConditions, on_delete=models.SET_NULL, null=True, blank=True)
  occasion = models.ForeignKey('wardrobe_manager.Occasion', on_delete=models.SET_NULL, null=True, blank=True)

class OutfitRecommendationResults(models.Model):
  recommendation = models.ForeignKey(OutfitRecommendations, on_delete=models.CASCADE)
  outfit = models.ForeignKey('wardrobe_manager.Outfit', on_delete=models.CASCADE)

"""
