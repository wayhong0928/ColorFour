from django.db import models

class WardrobeItem(models.Model):
    item_name = models.CharField(max_length=100) 
    item_type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField() 
    photo_url = models.CharField(max_length=255)
    tags = models.TextField(default='[]')
    garbage_can = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name


