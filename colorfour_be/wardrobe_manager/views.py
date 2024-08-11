from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WardrobeItem
from .serializers import WardrobeItemSerializer
from rest_framework.permissions import AllowAny

# 總覽 LIST
class WardrobeItemListCreate(generics.ListCreateAPIView):
	queryset = WardrobeItem.objects.filter(garbage_can=False).order_by("-created_at")
	serializer_class = WardrobeItemSerializer
	permission_classes = [AllowAny] # 此為暫時測試用，待第三方登入開發完成後移除。
	def perform_create(self, serializer):
		serializer.save()
		
# 垃圾桶裡的單品 LIST
class WardrobeItemListInGarbage(generics.ListCreateAPIView):
	queryset = WardrobeItem.objects.filter(garbage_can=True).order_by("-created_at")
	serializer_class = WardrobeItemSerializer
	permission_classes = [AllowAny] # 此為暫時測試用，待第三方登入開發完成後移除。

	def perform_create(self, serializer):
		serializer.save()

# 詳細、更新與刪除功能
class WardrobeItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = WardrobeItem.objects.all()
	serializer_class = WardrobeItemSerializer
	permission_classes = [AllowAny] # 此為暫時測試用，待第三方登入開發完成後移除。

	def delete(self, request, *args, **kwargs):
		item = self.get_object()
		if item.garbage_can:
			return super().delete(request, *args, **kwargs)
		else:
			item.garbage_can = True
			item.save()
			return Response({"message": "Item moved to garbage can"}, status=status.HTTP_200_OK)

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		return Response(serializer.data)

# 真正刪除垃圾桶中的單品
class DeleteFromGarbage(APIView):
	permission_classes = [AllowAny] # 此為暫時測試用，待第三方登入開發完成後移除。

	def delete(self, request, item_id):
		try:
			item = WardrobeItem.objects.get(id=item_id, garbage_can=True)
			item.delete()
			return Response({"message": "Item deleted permanently"}, status=status.HTTP_204_NO_CONTENT)
		except WardrobeItem.DoesNotExist:
			return Response({"error": "Item not found or not in garbage can"}, status=status.HTTP_404_NOT_FOUND)
