from django import forms
from .models import WardrobeItem

class WardrobeItemForm(forms.ModelForm):
  class Meta:
    model = WardrobeItem 

    fields = [
			"item_name",
			"item_type",
			"brand",
			"price",
			"created_at",
			"photo_url",
			"tags",
    ]