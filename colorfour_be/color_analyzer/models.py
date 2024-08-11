from django.db import models
from django.contrib.auth.models import User

class ColorAnalysis(models.Model):
  SEASON_CHOICES = [
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter'),
  ]
  
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
  season = models.CharField(max_length=7, choices=SEASON_CHOICES)
  skin_color = models.CharField(max_length=50)
  hair_color = models.CharField(max_length=50)
  eye_color = models.CharField(max_length=50)
  description = models.TextField()
  test_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user_id.username} - {self.season}"
