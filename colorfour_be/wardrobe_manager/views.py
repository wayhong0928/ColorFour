# colorfour_be/wardrobe_manager/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import (
    ClothMainCategory,
    ClothSubCategory,
    Color,
    Brand,
    ShoeCategory,
    ShoeSubCategory,
    Item,
    Occasion,
    ItemOccasion,
    Outfit,
    OutfitItem,
    OutfitOccasion,
)
from .serializers import (
    ClothMainCategorySerializer,
    ClothSubCategorySerializer,
    ShoeCategorySerializer,
    ShoeSubCategorySerializer,
    ItemSerializer,
    OccasionSerializer,
    ItemOccasionSerializer,
    OutfitSerializer,
    OutfitItemSerializer,
    OutfitOccasionSerializer,
    ColorSerializer,
    BrandSerializer,
)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def overview(self, request):
        """總攬畫面"""
        items = Item.objects.filter(user=self.request.user, is_in_trash=False)
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def trash(self, request):
        """獲取垃圾桶中的項目"""
        trash_items = Item.objects.filter(user=self.request.user, is_in_trash=True)
        serializer = self.get_serializer(trash_items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def move_to_trash(self, request, pk=None):
        """將項目移到垃圾桶"""
        item = self.get_object()
        if item.user != request.user:
            return Response({"error": "你沒有權限移動此項目"}, status=403)
        item.is_in_trash = True
        item.save()
        return Response({"status": "moved to trash"})

    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        """從垃圾桶恢復項目"""
        item = self.get_object()
        if item.user != request.user:
            return Response({"error": "你沒有權限恢復此項目"}, status=403)
        item.is_in_trash = False
        item.save()
        return Response({"status": "restored from trash"})

    @action(detail=True, methods=["delete"])
    def permanent_delete(self, request, pk=None):
        """永久刪除項目"""
        item = self.get_object()
        if item.user != request.user:
            return Response({"error": "你沒有權限刪除此項目"}, status=403)
        item.delete()
        return Response({"status": "permanently deleted"})


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticated]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


class OccasionViewSet(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer
    permission_classes = [IsAuthenticated]


class ItemOccasionViewSet(viewsets.ModelViewSet):
    queryset = ItemOccasion.objects.all()
    serializer_class = ItemOccasionSerializer
    permission_classes = [IsAuthenticated]


class OutfitViewSet(viewsets.ModelViewSet):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
    permission_classes = [IsAuthenticated]


class OutfitItemViewSet(viewsets.ModelViewSet):
    queryset = OutfitItem.objects.all()
    serializer_class = OutfitItemSerializer
    permission_classes = [IsAuthenticated]


class OutfitOccasionViewSet(viewsets.ModelViewSet):
    queryset = OutfitOccasion.objects.all()
    serializer_class = OutfitOccasionSerializer
    permission_classes = [IsAuthenticated]


class ClothCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClothMainCategory.objects.all()
    serializer_class = ClothMainCategorySerializer
    permission_classes = [IsAuthenticated]


class ClothSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClothSubCategory.objects.all()
    serializer_class = ClothSubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        main_category = self.request.GET.get("main_category", None)
        if main_category is not None:
            return self.queryset.filter(main_category_id=main_category)
        return self.queryset


class ShoeCategoryViewSet(viewsets.ModelViewSet):
    queryset = ShoeCategory.objects.all()
    serializer_class = ShoeCategorySerializer
    permission_classes = [IsAuthenticated]


class ShoeSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ShoeSubCategory.objects.all()
    serializer_class = ShoeSubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        shoe_category = self.request.GET.get("shoe_category", None)
        if shoe_category is not None:
            return self.queryset.filter(shoe_category_id=shoe_category)
        return self.queryset
