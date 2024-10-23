from rest_framework import serializers
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
    Notification,
)


class UserFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollower
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "content", "media_url", "location", "created_at"]
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user  # 自動設置 user
        return super().create(validated_data)


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "post",
            "content",
            "created_at",
        ]  # 不包含 user，因為 user 是後端自動填入的


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = "__all__"


class PostBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostBookmark
        fields = "__all__"


class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDelete
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
