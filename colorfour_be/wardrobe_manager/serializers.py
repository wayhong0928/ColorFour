from rest_framework import serializers
from .models import WardrobeItem


class WardrobeItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = WardrobeItem
		fields = [
			"id",
			"item_name",
			"item_type",
			"brand",
			"price",
			"created_at",
			"photo_url",
			"tags",
			"garbage_can",
		]
