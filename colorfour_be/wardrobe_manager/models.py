from django.db import models

class WardrobeItem(models.Model):
  user_id = models.IntegerField()
  item_name = models.CharField(max_length=100)
  item_type = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  purchase_date = models.DateField()
  photo_url = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.item_name


