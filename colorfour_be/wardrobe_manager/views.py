from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    WardrobeCategory,
    WardrobeType,
    WardrobeItem,
    WardrobeOccasion,
    WardrobeItemOccasion,
    WardrobeOutfit,
    WardrobeOutfitItem,
    WardrobeOutfitOccasion,
)
from .serializers import (
    WardrobeCategorySerializer,
    WardrobeTypeSerializer,
    WardrobeItemSerializer,
    WardrobeOccasionSerializer,
    WardrobeItemOccasionSerializer,
    WardrobeOutfitSerializer,
    WardrobeOutfitItemSerializer,
    WardrobeOutfitOccasionSerializer,
)


class WardrobeCategoryViewSet(viewsets.ModelViewSet):
    queryset = WardrobeCategory.objects.all()
    serializer_class = WardrobeCategorySerializer


class WardrobeTypeViewSet(viewsets.ModelViewSet):
    queryset = WardrobeType.objects.all()
    serializer_class = WardrobeTypeSerializer


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import WardrobeItem
from .serializers import WardrobeItemSerializer

class WardrobeItemViewSet(viewsets.ModelViewSet):
  queryset = WardrobeItem.objects.filter(is_in_trash=False)  # 過濾掉垃圾桶內的項目
  serializer_class = WardrobeItemSerializer

  @action(detail=False, methods=['get'])
  def overview(self, request):
    """總攬畫面"""
    items = self.get_queryset()
    serializer = self.get_serializer(items, many=True)
    return Response(serializer.data)

  def retrieve(self, request, *args, **kwargs):
    """詳細資料頁面"""
    item = self.get_object()
    serializer = self.get_serializer(item)
    return Response(serializer.data)

  @action(detail=False, methods=["get"])
  def trash(self, request):
    """獲取垃圾桶中的項目"""
    trash_items = WardrobeItem.objects.filter(is_in_trash=True)
    serializer = self.get_serializer(trash_items, many=True)
    return Response(serializer.data)

  @action(detail=True, methods=["post"])
  def move_to_trash(self, request, pk=None):
    """將項目移到垃圾桶"""
    item = self.get_object()
    item.is_in_trash = True
    item.save()
    return Response({"status": "moved to trash"})

  @action(detail=True, methods=["post"])
  def restore(self, request, pk=None):
    """從垃圾桶恢復項目"""
    item = self.get_object()
    item.is_in_trash = False
    item.save()
    return Response({"status": "restored from trash"})

  @action(detail=True, methods=["delete"])
  def permanent_delete(self, request, pk=None):
    """永久刪除項目"""
    item = self.get_object()
    item.delete()
    return Response({"status": "permanently deleted"})


class WardrobeOccasionViewSet(viewsets.ModelViewSet):
    queryset = WardrobeOccasion.objects.all()
    serializer_class = WardrobeOccasionSerializer


class WardrobeItemOccasionViewSet(viewsets.ModelViewSet):
    queryset = WardrobeItemOccasion.objects.all()
    serializer_class = WardrobeItemOccasionSerializer


class WardrobeOutfitViewSet(viewsets.ModelViewSet):
    queryset = WardrobeOutfit.objects.all()
    serializer_class = WardrobeOutfitSerializer


class WardrobeOutfitItemViewSet(viewsets.ModelViewSet):
    queryset = WardrobeOutfitItem.objects.all()
    serializer_class = WardrobeOutfitItemSerializer


class WardrobeOutfitOccasionViewSet(viewsets.ModelViewSet):
    queryset = WardrobeOutfitOccasion.objects.all()
    serializer_class = WardrobeOutfitOccasionSerializer
