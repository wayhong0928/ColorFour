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
    main_category = serializers.PrimaryKeyRelatedField(
        queryset=ClothMainCategory.objects.all(), allow_null=True
    )
    sub_category = serializers.PrimaryKeyRelatedField(
        queryset=ClothSubCategory.objects.all(), allow_null=True
    )
    shoe_category = serializers.PrimaryKeyRelatedField(
        queryset=ShoeCategory.objects.all(), allow_null=True
    )
    shoe_sub_category = serializers.PrimaryKeyRelatedField(
        queryset=ShoeSubCategory.objects.all(), allow_null=True
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), required=True
    )
    color = serializers.PrimaryKeyRelatedField(
        queryset=Color.objects.all(), required=True
    )
    occasions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Occasion.objects.all(), required=False
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "item_name",
            "main_category",
            "sub_category",
            "shoe_category",
            "shoe_sub_category",
            "brand",
            "color",
            "price",
            "content",
            "photo_url",
            "purchase_link",
            "is_in_trash",
            "is_in_love",
            "add_date",
            "edit_date",
            "occasions",
        ]

    def create(self, validated_data):
        occasions_data = validated_data.pop("occasions", [])
        item = Item.objects.create(**validated_data)
        item.occasions.set(occasions_data)
        return item

    def update(self, instance, validated_data):
        occasions_data = validated_data.pop("occasions", None)
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
    items = serializers.SerializerMethodField()

    class Meta:
        model = Outfit
        fields = [
            "id",
            "outfit_name",
            "description",
            "outfit_image",
            "items",
            "created_at",
            "latest_edit",
        ]

    def create(self, validated_data):
        # 取出 selected_items，剩餘資料用於建立 Outfit
        selected_items = validated_data.pop("selected_items", [])
        outfit = Outfit.objects.create(**validated_data)

        # 為每個選中的 Item 建立 OutfitItem 關聯
        outfit_items = [
            OutfitItem(outfit=outfit, item_id=item_id) for item_id in selected_items
        ]
        OutfitItem.objects.bulk_create(outfit_items)  # 批量建立關聯

        return outfit

    def get_items(self, obj):
        outfit_items = OutfitItem.objects.filter(outfit=obj).select_related("item")
        return ItemSerializer(
            [outfit_item.item for outfit_item in outfit_items], many=True
        ).data


# 最愛穿搭與服裝單品關聯
class OutfitItemSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    class Meta:
        model = OutfitItem
        fields = "__all__"


# 最愛穿搭與場合標籤關聯
class OutfitOccasionSerializer(serializers.ModelSerializer):
    outfit = OutfitSerializer(read_only=True)
    occasion = OccasionSerializer(read_only=True)

    class Meta:
        model = OutfitOccasion
        fields = "__all__"
