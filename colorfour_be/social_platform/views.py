from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Post, PostBookmark, UserFollower, Comment
from django.shortcuts import get_object_or_404
from .serializers import (
    PostSerializer,
    PostBookmarkSerializer,
    UserFollowerSerializer,
    CommentSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 確保使用者已登入


    @action(detail=False, methods=['get'], url_path='bookmarked')
    def bookmarked_posts(self, request):
        """取得使用者收藏的貼文"""
        bookmarks = PostBookmark.objects.filter(user=request.user).select_related('post')
        serializer = PostSerializer([bookmark.post for bookmark in bookmarks], many=True)
        return Response(serializer.data)

    # 自訂的首頁貼文，根據建立時間排序
    @action(detail=False, methods=['get'])
    def homepage(self, request):
        posts = self.get_queryset().order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class UserFollowerViewSet(viewsets.ModelViewSet):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerSerializer

    @action(detail=False, methods=["get"])
    def follow_overview(self, request):
        """顯示追蹤總覽"""
        user = request.user
        followers = UserFollower.objects.filter(following=user)
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"], url_path="toggle")
    def toggle_follow(self, request):
        """追蹤或取消追蹤使用者"""
        follower = request.user
        followed_user_id = request.data.get("user")
        followed_user = get_object_or_404(settings.AUTH_USER_MODEL, id=followed_user_id)

        # 檢查是否已追蹤
        follow_instance, created = UserFollower.objects.get_or_create(
            follower=follower, followed_user=followed_user
        )
        if not created:
            follow_instance.delete()  # 取消追蹤
            return Response({"status": "unfollowed"})
        return Response({"status": "followed"})
