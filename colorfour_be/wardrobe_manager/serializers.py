from rest_framework import serializers
from .models import (
    WardrobeCategory,
    WardrobeType,
    WardrobeItem,
    WardrobeOccasion,
    WardrobeItemOccasion,
    WardrobeOutfit,
    WardrobeOutfitItem,
    WardrobeOutfitOccasion,
)

#新增服飾功能
class WardrobeItemCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = WardrobeItem
    fields = ['id', 'user', 'item_name', 'brand', 'color', 'price', 'purchase_date', 'Label', 'photo_url', 'is_in_trash', 'created_at', 'latest_edit']
    read_only_fields = ['user', 'created_at', 'latest_edit']

  def create(self, validated_data):
    # 如果需要，這裡可以自動填入購買日期
    # if 'purchase_date' not in validated_data:
    #   validated_data['purchase_date'] = datetime.date.today()
    return super().create(validated_data)


class WardrobeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeCategory
        fields = "__all__"


class WardrobeTypeSerializer(serializers.ModelSerializer):
    category = WardrobeCategorySerializer()

    class Meta:
        model = WardrobeType
        fields = "__all__"


class WardrobeItemSerializer(serializers.ModelSerializer):
    type = WardrobeTypeSerializer()

    class Meta:
        model = WardrobeItem
        fields = "__all__"


class WardrobeOccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardrobeOccasion
        fields = "__all__"


class WardrobeItemOccasionSerializer(serializers.ModelSerializer):
    item = WardrobeItemSerializer()
    occasion = WardrobeOccasionSerializer()

    class Meta:
        model = WardrobeItemOccasion
        fields = "__all__"


class WardrobeOutfitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = WardrobeOutfit
        fields = "__all__"


class WardrobeOutfitItemSerializer(serializers.ModelSerializer):
    outfit = WardrobeOutfitSerializer()
    item = WardrobeItemSerializer()

    class Meta:
        model = WardrobeOutfitItem
        fields = "__all__"


class WardrobeOutfitOccasionSerializer(serializers.ModelSerializer):
    outfit = WardrobeOutfitSerializer()
    occasion = WardrobeOccasionSerializer()

    class Meta:
        model = WardrobeOutfitOccasion
        fields = "__all__"
