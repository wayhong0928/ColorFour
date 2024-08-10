from django.shortcuts import render, redirect 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from .models import WardrobeItem 
from .forms import WardrobeItemForm
from .serializers import WardrobeItemSerializer
import json


# 新增衣服
def add_wardrobe_item(request):
	if request.method == 'POST':
		form = WardrobeItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_wardrobe_item')
	else:
		# 如果請求方法不是POST，則創建一個空表單
		form = WardrobeItemForm()
	# 渲染模板並傳遞表單到模板上下文
	return render(request, 'wardrobe/add_wardrobe_item.html', {'form': form})


# 刪除衣服
@method_decorator(csrf_exempt, name='dispatch')
class DeleteWardrobeItemView(View):
	def delete(self, request, item_id):
		try:
			item = WardrobeItem.objects.get(id=item_id)
			item.delete()  # 如果資料存在，則刪除該資料
			return JsonResponse({'message': 'Item deleted successfully!'}, status=200)
		except WardrobeItem.DoesNotExist:
			return JsonResponse({'error': 'Item not found!'}, status=404)

#丟到垃圾桶
@method_decorator(csrf_exempt, name='dispatch')
class MoveToGarbageView(View):
  def post(self, request, item_id):
    try:
      item = WardrobeItem.objects.get(id=item_id)
      item.garbage_can = True  #Call就會把garbage_can改成True就是丟到垃圾桶了
      item.save()
      return JsonResponse({'message': 'Item moved to garbage can successfully!'}, status=200)
    except WardrobeItem.DoesNotExist:
      return JsonResponse({'error': 'Item not found!'}, status=404)


# 修改衣服
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
