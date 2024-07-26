# wardrobe_manager/serializers.py

from rest_framework import serializers
from .models import WardrobeItem

class WardrobeItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = WardrobeItem
    fields = [
      'user_id',
      'item_name',
      'item_type',
      'brand',
      'color',
      'price',
      'purchase_date',
      'photo_url'
    ]
