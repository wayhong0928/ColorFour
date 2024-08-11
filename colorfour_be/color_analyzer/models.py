from django.db import models
from django.contrib.auth.models import User

class ColorAnalysis(models.Model):
  SEASON_CHOICES = [
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter'),
  ]
  
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')  # 將 user_id 改為 ForeignKey
  season = models.CharField(max_length=7, choices=SEASON_CHOICES)  # 將 max_length 改為 7 以容納 'Autumn'
  skin_color = models.CharField(max_length=50)
  hair_color = models.CharField(max_length=50)
  eye_color = models.CharField(max_length=50)
  description = models.TextField()
  test_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user_id.username} - {self.season}"  # user_id 變為 ForeignKey 後，可以直接訪問 username
