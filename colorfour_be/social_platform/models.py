from django.db import models
from django.conf import settings

class UserFollower(models.Model):
  follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
  followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('follower', 'followed_user')
    db_table = 'social_platform_userfollower'


class Tag(models.Model):
  tag_name = models.CharField(max_length=100, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_tag'


class Post(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField(blank=True, null=True)
  media_url = models.ImageField(upload_to='post_media', blank=True, null=True)
  media_type = models.CharField(max_length=20, blank=True, null=True)
  link_url = models.CharField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_post'


class PostTag(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = ('post', 'tag')
    db_table = 'social_platform_posttag'


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_comment'


class PostLike(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_postlike'


class PostShare(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  shared_on = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_postshare'


class PostBookmark(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'social_platform_postbookmark'


class PostDelete(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  deleted_at = models.DateTimeField(auto_now_add=True)
  expiry_at = models.DateTimeField()

  class Meta:
    db_table = 'social_platform_postdelete'


class Message(models.Model):
  sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
  receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_read = models.BooleanField(default=False)

  class Meta:
    db_table = 'social_platform_message'

'''
原來生成的資料庫，但在migrate時會有錯誤，以下是chatgpt的解釋
這個錯誤訊息表示在 Notification 模型中，related_user 和 user 這兩個字段都與 User 模型建立了 ForeignKey 關聯，並且都使用了預設的反向關聯名稱 notification_set，這會導致 Django 無法區分這兩個字段的反向關聯。


class Notification(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  trigger_event = models.CharField(max_length=50)
  related_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
  related_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  is_read = models.BooleanField(default=False)
  linebot_notified = models.BooleanField(default=False)

  class Meta:
    db_table = 'social_platform_notification'
'''
""" 改動過後的 """
class Notification(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
  related_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='related_notifications')
  content = models.TextField()
  trigger_event = models.CharField(max_length=50)
  related_post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  is_read = models.BooleanField(default=False)
  linebot_notified = models.BooleanField(default=False)

  class Meta:
    db_table = 'social_platform_notification'

"""
解決方法:
你需要為其中一個或兩個 ForeignKey 字段添加 related_name 參數，以避免反向關聯名稱的衝突。related_name 允許你自定義在 User 模型中的反向關聯名稱。


改動解釋:

在這裡，user 字段的反向關聯名稱被設置為 notifications，而 related_user 字段的反向關聯名稱被設置為 related_notifications。這樣，Django 就能區分這兩個字段的反向關聯，不會再發生衝突。

影響範圍：

這個改動會影響到你在使用反向關聯時的查詢，比如：

user.notifications.all()  # 取得 user 的所有通知
related_user.related_notifications.all()  # 取得和 related_user 相關的通知
"""