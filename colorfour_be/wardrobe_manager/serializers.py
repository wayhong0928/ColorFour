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
