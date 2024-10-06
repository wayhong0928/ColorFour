from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    Post, PostBookmark, UserFollower, Comment
)
from .serializers import (
    PostSerializer, PostBookmarkSerializer, UserFollowerSerializer, CommentSerializer
)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def homepage(self, request):
        """顯示首頁，通常顯示最新或熱門貼文"""
        posts = self.get_queryset().order_by('-created_at')  # 根據建立時間排序
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def user_page(self, request):
        """顯示個人頁面，顯示該使用者的所有貼文"""
        user = request.user
        user_posts = Post.objects.filter(user=user)
        serializer = self.get_serializer(user_posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def bookmark(self, request, pk=None):
        """收藏貼文"""
        post = self.get_object()
        bookmark, created = PostBookmark.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({"status": "post bookmarked"})
        return Response({"status": "post already bookmarked"})

    def create(self, request, *args, **kwargs):
        """新增貼文"""
        data = request.data
        data['user'] = request.user.id  # 自動將當前使用者設為貼文作者
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, *args, **kwargs):
        """修改貼文"""
        post = self.get_object()
        if post.user != request.user:
            return Response({"error": "You cannot edit this post"}, status=403)
        return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        """新增留言"""
        post = self.get_object()
        data = request.data
        data['post'] = post.id  # 將當前貼文自動設定為留言所屬的貼文
        data['user'] = request.user.id  # 自動將當前使用者設定為留言作者
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "comment added", "comment": serializer.data})
        return Response(serializer.errors, status=400)


class UserFollowerViewSet(viewsets.ModelViewSet):
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerSerializer

    @action(detail=False, methods=['get'])
    def follow_overview(self, request):
        """顯示追蹤總覽"""
        user = request.user
        followers = UserFollower.objects.filter(following=user)
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)
