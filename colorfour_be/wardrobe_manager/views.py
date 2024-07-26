from django.shortcuts import render, redirect  # render用於渲染模板，redirect用於重定向
from .models import WardrobeItem  # 引入WardrobeItem模型
from .forms import WardrobeItemForm  # 引入WardrobeItemForm表單

# 刪除資料的import
from django.http import JsonResponse
from django.views import View

# 修改資料的import
import json

# 測試API *
from rest_framework import generics
from .serializers import WardrobeItemSerializer

# 測試刪除用的 *之後必須刪除因為會有安全性的問題
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# 新增衣服
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


# 刪除衣服
# 這行是測試用的禁用CSRF保護(就是這行不知道會不會有安全性的問題)  我的@csrf_exempt需要用 @method_decorator包裝
@method_decorator(csrf_exempt, name='dispatch')
class DeleteWardrobeItemView(View):
    def delete(self, request, item_id):
        try:
            # 嘗試從 WardrobeItem 模型中根據傳入的 item_id 取得相應的資料
            item = WardrobeItem.objects.get(id=item_id)
            item.delete()  # 如果資料存在，則刪除該資料
            return JsonResponse({'message': 'Item deleted successfully!'}, status=200)
        except WardrobeItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found!'}, status=404)


# 修改衣服
# 這行是測試用的禁用CSRF保護(就是這行不知道會不會有安全性的問題)  我的@csrf_exempt需要用 @method_decorator包裝
@method_decorator(csrf_exempt, name='dispatch')
class UpdateWardrobeItemView(View):
    def put(self, request, item_id):
        try:
            item = WardrobeItem.objects.get(id=item_id)
        except WardrobeItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found!'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return JsonResponse({'error': 'Invalid JSON data!'}, status=400)

        item.item_name = data.get('item_name', item.item_name)
        item.item_type = data.get('item_type', item.item_type)
        item.brand = data.get('brand', item.brand)
        item.color = data.get('color', item.color)
        item.price = data.get('price', item.price)
        item.purchase_date = data.get('purchase_date', item.purchase_date)
        item.photo_url = data.get('photo_url', item.photo_url)

        item.save()

        return JsonResponse({'message': 'Item updated successfully!'}, status=200)


# 測試API *
class WardrobeItemListCreate(generics.ListCreateAPIView):
    queryset = WardrobeItem.objects.all()
    serializer_class = WardrobeItemSerializer
