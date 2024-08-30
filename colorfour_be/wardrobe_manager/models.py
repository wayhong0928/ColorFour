from django.db import models
from django.conf import settings


class WardrobeCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class WardrobeType(models.Model):
    category = models.ForeignKey(WardrobeCategory, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=100, unique=True)
    temperature = models.IntegerField()

    def __str__(self):
        return self.type_name


class WardrobeItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.ForeignKey(
        WardrobeType, on_delete=models.CASCADE, null=True, blank=True
    )
    item_name = models.CharField(max_length=20)
    brand = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    is_in_trash = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    latest_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class WardrobeOccasion(models.Model):
    occasion_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.occasion_name


class WardrobeItemOccasion(models.Model):
    item = models.ForeignKey(WardrobeItem, on_delete=models.CASCADE)
    occasion = models.ForeignKey(WardrobeOccasion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("item", "occasion")


class WardrobeOutfit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    outfit_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    latest_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.outfit_name


class WardrobeOutfitItem(models.Model):
    outfit = models.ForeignKey(WardrobeOutfit, on_delete=models.CASCADE)
    item = models.ForeignKey(WardrobeItem, on_delete=models.CASCADE)


class WardrobeOutfitOccasion(models.Model):
    outfit = models.ForeignKey(WardrobeOutfit, on_delete=models.CASCADE)
    occasion = models.ForeignKey(WardrobeOccasion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("outfit", "occasion")
