from django.shortcuts import render, redirect
from .models import ColorAnalysis
from .forms import ColorAnalysisForm

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import random  # random加入季節


# 新增色彩分析資料
@csrf_exempt
def add_color_analysis(request):
	if request.method == "POST":
		try:
			data = json.loads(request.body.decode("utf-8"))  # 從請求中解析JSON數據

			# 手動設置 user_id 和 season
			data["user_id"] = 1  # 假設用戶ID為1
			data["season"] = random.choice(
				["Spring", "Summer", "Autumn", "Winter"]
			)  # 隨機選擇季節

			form = ColorAnalysisForm(data)  # 將處理過的數據傳遞給表單

			if form.is_valid():
				form.save()  # 保存數據到資料庫
				return JsonResponse(
					{"message": "Color analysis added successfully!"}, status=201
				)
			else:
				return JsonResponse(
					{"error": "Invalid form data", "details": form.errors}, status=400
				)
		except json.JSONDecodeError as e:
			return JsonResponse(
				{"error": "Invalid JSON data", "details": str(e)}, status=400
			)
		except Exception as e:
			return JsonResponse(
				{"error": "Internal server error", "details": str(e)}, status=500
			)
	return JsonResponse({"error": "Invalid request method"}, status=405)


""""
原來的色彩分析add
def add_color_analysis(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body.decode('utf-8'))  # 從請求中解析JSON數據
			form = ColorAnalysisForm(data) # 將數據傳遞給表單
			if form.is_valid():
				form.save()  # 如果表單有效，保存數據到資料庫
				return JsonResponse({'message': 'Color analysis added successfully!'}, status=201)
			else:
				return JsonResponse({'error': 'Invalid form data', 'details': form.errors}, status=400)
		except json.JSONDecodeError as e:
			return JsonResponse({'error': 'Invalid JSON data', 'details': str(e)}, status=400)
		except Exception as e:
			return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
	return JsonResponse({'error': 'Invalid request method'}, status=405)
"""


# 刪除色彩分析資料
@method_decorator(csrf_exempt, name="dispatch")
class DeleteColorAnalysisView(View):
	def delete(self, request, item_id):
		try:
			item = ColorAnalysis.objects.get(id=item_id)  # 根據ID查找資料
			item.delete()  # 刪除資料
			return JsonResponse({"message": "Item deleted successfully!"}, status=200)
		except ColorAnalysis.DoesNotExist:
			return JsonResponse({"error": "Item not found!"}, status=404)
		except Exception as e:
			return JsonResponse(
				{"error": "Internal server error", "details": str(e)}, status=500
			)
