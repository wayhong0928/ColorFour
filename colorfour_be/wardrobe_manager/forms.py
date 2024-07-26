from django import forms
from .models import WardrobeItem

class WardrobeItemForm(forms.ModelForm):
  class Meta:
    model = WardrobeItem 

    fields = [
      'user_id',          # 使用者ID
      'item_name',        # 物品名稱
      'item_type',        # 物品類型
      'brand',            # 品牌
      'color',            # 顏色
      'price',            # 價格
      'purchase_date',    # 購買日期
      'photo_url'         # 照片URL
    ]