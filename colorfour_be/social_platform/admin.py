from django.contrib import admin
from .models import (
  UserFollower,
  Tag,
  Post,
  PostTag,
  Comment,
  PostLike,
  PostShare,
  PostBookmark,
  PostDelete,
  Message,
  Notification
)

# @admin.register(UserFollower)
# class UserFollowerAdmin(admin.ModelAdmin):
#   list_display = ('follower', 'followed_user', 'created_at')
#   search_fields = ('follower__username', 'followed_user__username')

# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#   list_display = ('tag_name', 'created_at')
#   search_fields = ('tag_name',)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#   list_display = ('user', 'content', 'media_type', 'created_at')
#   search_fields = ('user__username', 'content')
#   list_filter = ('media_type', 'created_at')

# @admin.register(PostTag)
# class PostTagAdmin(admin.ModelAdmin):
#   list_display = ('post', 'tag', 'created_at')
#   search_fields = ('post__content', 'tag__tag_name')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#   list_display = ('post', 'user', 'content', 'created_at')
#   search_fields = ('post__content', 'user__username')

# @admin.register(PostLike)
# class PostLikeAdmin(admin.ModelAdmin):
#   list_display = ('post', 'user', 'created_at')
#   search_fields = ('post__content', 'user__username')

# @admin.register(PostShare)
# class PostShareAdmin(admin.ModelAdmin):
#   list_display = ('post', 'user', 'shared_on', 'created_at')
#   search_fields = ('post__content', 'user__username', 'shared_on')

# @admin.register(PostBookmark)
# class PostBookmarkAdmin(admin.ModelAdmin):
#   list_display = ('post', 'user', 'created_at')
#   search_fields = ('post__content', 'user__username')

# @admin.register(PostDelete)
# class PostDeleteAdmin(admin.ModelAdmin):
#   list_display = ('post', 'user', 'deleted_at', 'expiry_at')
#   search_fields = ('post__content', 'user__username')

# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#   list_display = ('sender', 'receiver', 'content', 'created_at', 'is_read')
#   search_fields = ('sender__username', 'receiver__username', 'content')

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#   list_display = ('user', 'content', 'trigger_event', 'created_at', 'is_read', 'linebot_notified')
#   search_fields = ('user__username', 'content', 'trigger_event')

