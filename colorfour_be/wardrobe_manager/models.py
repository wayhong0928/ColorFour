from django.db import models
from django.conf import settings

class ClothMainCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClothSubCategory(models.Model):
    main_category = models.ForeignKey(
        ClothMainCategory, on_delete=models.CASCADE, related_name="subcategories"
    )
    name = models.CharField(max_length=100)
    temperature = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.main_category.name} - {self.name}"

class ShoeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ShoeSubCategory(models.Model):
    shoe_category = models.ForeignKey(
        ShoeCategory,
        on_delete=models.CASCADE,
        related_name="shoe_subcategories",
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.shoe_category.name} - {self.name}"

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=False)
    main_category = models.ForeignKey(ClothMainCategory, on_delete=models.CASCADE, null=True)
    sub_category = models.ForeignKey(ClothSubCategory, on_delete=models.CASCADE, null=True)
    shoe_category = models.ForeignKey(ShoeCategory, on_delete=models.CASCADE, null=True)
    shoe_sub_category = models.ForeignKey(ShoeSubCategory, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    occasions = models.ManyToManyField("Occasion", through="ItemOccasion", related_name="items")
    purchase_date = models.DateField(auto_now_add=True, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    photo_url = models.ImageField(upload_to="wardrobe_items/", blank=True, null=True)
    purchase_link = models.CharField(max_length=255, blank=True, null=True)
    is_in_trash = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} - {self.sub_category} - {self.content}"


class Occasion(models.Model):
    occasion_name = models.CharField(max_length=100, default="未命名")

    def __str__(self):
        return self.occasion_name


class ItemOccasion(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("item", "occasion")


class Outfit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    outfit_name = models.CharField(max_length=50, default="未命名")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    latest_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.outfit_name


class OutfitItem(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class OutfitOccasion(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("outfit", "occasion")
