from django.shortcuts import render, redirect 
from .models import WardrobeItem 
from .forms import WardrobeItemForm

from rest_framework import generics
from .serializers import WardrobeItemSerializer 

def add_wardrobe_item(request):
  if request.method == 'POST':
    form = WardrobeItemForm(request.POST)
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

