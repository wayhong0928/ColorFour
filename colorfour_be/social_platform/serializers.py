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
        fields = ["id", "tag_name"]


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ["id", "content", "media_url", "location", "tags", "created_at"]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        post = Post.objects.create(**validated_data)

        post.tags.set(tags_data)

        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags", [])
        instance = super().update(instance, validated_data)
        instance.tags.set(tags_data)
        return instance


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
        ]


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
