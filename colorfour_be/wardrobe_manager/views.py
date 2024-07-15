from django.shortcuts import render, redirect  # render用於渲染模板，redirect用於重定向
from .models import WardrobeItem  # 引入WardrobeItem模型
from .forms import WardrobeItemForm  # 引入WardrobeItemForm表單

#測試API *
from rest_framework import generics
from .serializers import WardrobeItemSerializer 

# 定義一個視圖函數來處理新增衣服項目
def add_wardrobe_item(request):
  # 檢查請求方法是否為POST
  if request.method == 'POST':
    # 如果是POST方法，則使用提交的數據創建表單實例
    form = WardrobeItemForm(request.POST)
    # 檢查表單是否有效
    if form.is_valid():
      # 如果表單有效，則保存數據到資料庫
      form.save()
      # 保存後重定向到新增頁面或其他頁面
      return redirect('add_wardrobe_item')
  else:
    # 如果請求方法不是POST，則創建一個空表單
    form = WardrobeItemForm()
  # 渲染模板並傳遞表單到模板上下文
  return render(request, 'wardrobe/add_wardrobe_item.html', {'form': form})

#測試API *
class WardrobeItemListCreate(generics.ListCreateAPIView):
    queryset = WardrobeItem.objects.all()
    serializer_class = WardrobeItemSerializer

