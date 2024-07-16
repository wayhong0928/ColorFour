from django import forms  # 引入Django的forms模組，用於創建表單
from .models import WardrobeItem  # 引入WardrobeItem模型，這是我們在表單中使用的模型

# 定義一個表單類來處理WardrobeItem模型的數據
class WardrobeItemForm(forms.ModelForm):
  # Meta類用於指定表單的一些基本配置
  class Meta:
    model = WardrobeItem  # 指定這個表單是基於WardrobeItem模型的

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

#from.py是為了定義表單類。這些表單類基於Django的表單API（即 django.forms）
#在 wardrobe/forms.py 中定義表單類後，可以在視圖中(view.py)使用這個表單類來處理用戶提交的數據。


