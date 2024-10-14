# colorfour_be/wardrobe_manager/serializers.py
from rest_framework import serializers
from .models import (
    Item,
    Occasion,
    ItemOccasion,
    Outfit,
    OutfitItem,
    OutfitOccasion,
    ClothMainCategory,
    ClothSubCategory,
    ShoeCategory,
    ShoeSubCategory,
    Brand,
    Color,
)


# 主要服裝類別
class ClothMainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothMainCategory
        fields = "__all__"


# 次要服裝類別
class ClothSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothSubCategory
        fields = "__all__"


# 鞋子主要類別
class ShoeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeCategory
        fields = "__all__"


# 鞋子次要類別
class ShoeSubCategorySerializer(serializers.ModelSerializer):
    shoe_category = ShoeCategorySerializer()

    class Meta:
        model = ShoeSubCategory
        fields = "__all__"


# 品牌
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


# 顏色
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


# 服裝單品
class ItemSerializer(serializers.ModelSerializer):
    main_category = serializers.PrimaryKeyRelatedField(queryset=ClothMainCategory.objects.all(), allow_null=True)
    sub_category = serializers.PrimaryKeyRelatedField(queryset=ClothSubCategory.objects.all(), allow_null=True)
    shoe_category = serializers.PrimaryKeyRelatedField(queryset=ShoeCategory.objects.all(), allow_null=True)
    shoe_sub_category = serializers.PrimaryKeyRelatedField(queryset=ShoeSubCategory.objects.all(), allow_null=True)
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), required=True)
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), required=True)
    occasions = serializers.PrimaryKeyRelatedField(many=True, queryset=Occasion.objects.all(), required=False)

    class Meta:
        model = Item
        fields = [
            'id', 'item_name', 'main_category', 'sub_category', 'shoe_category',
            'shoe_sub_category', 'brand', 'color', 'price', 'content', 'photo_url',
            'purchase_link', 'is_in_trash', 'add_date', 'edit_date', 'occasions'
        ]
    
    def create(self, validated_data):
        occasions_data = validated_data.pop('occasions', [])
        item = Item.objects.create(**validated_data)
        item.occasions.set(occasions_data)
        return item

    def update(self, instance, validated_data):
        occasions_data = validated_data.pop('occasions', None)
        if occasions_data is not None:
            instance.occasions.set(occasions_data)
        return super().update(instance, validated_data)


# 場合標籤
class OccasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = "__all__"


# 服裝單品與場合標籤關聯
class ItemOccasionSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    occasion = OccasionSerializer()

    class Meta:
        model = ItemOccasion
        fields = "__all__"


# 最愛穿搭
class OutfitSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Outfit
        fields = "__all__"


# 最愛穿搭與服裝單品關聯
class OutfitItemSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer()
    item = ItemSerializer()

    class Meta:
        model = OutfitItem
        fields = "__all__"


# 最愛穿搭與場合標籤關聯
class OutfitOccasionSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer()
    occasion = OccasionSerializer()

    class Meta:
        model = OutfitOccasion
        fields = "__all__"
