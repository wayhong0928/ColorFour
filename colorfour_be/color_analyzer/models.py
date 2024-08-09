from django.db import models

class ColorAnalysis(models.Model):
  SEASON_CHOICES = [
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter'),
  ]
  
  user_id = models.IntegerField()  # 確保有這個欄位
  season = models.CharField(max_length=6, choices=SEASON_CHOICES)
  skin_color = models.CharField(max_length=50)
  hair_color = models.CharField(max_length=50)
  eye_color = models.CharField(max_length=50)
  description = models.TextField()
  test_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user_id} - {self.season}"
