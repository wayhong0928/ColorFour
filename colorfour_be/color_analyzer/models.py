from django.db import models
from django.conf import settings

class ColorAnalysis(models.Model):
  SEASON_CHOICES = [
    ('Spring', 'Spring'),
    ('Summer', 'Summer'),
    ('Autumn', 'Autumn'),
    ('Winter', 'Winter'),
  ]
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
  season = models.CharField(max_length=7, choices=SEASON_CHOICES)
  skin_color = models.CharField(max_length=50)
  hair_color = models.CharField(max_length=50)
  eye_color = models.CharField(max_length=50)
  description = models.TextField()
  test_date = models.DateTimeField(auto_now_add=True)
  fitness_problem1 = models.CharField(max_length=100, blank=True, null=True) #blank=true 不提供這些欄位的值時仍然通過驗證
  fitness_problem2 = models.CharField(max_length=100, blank=True, null=True) #null=True 沒有提供這些欄位的值時保存為 NULL
  fitness_problem3 = models.CharField(max_length=100, blank=True, null=True)
  fitness_problem4 = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return f"{self.user.username} - {self.season}"
