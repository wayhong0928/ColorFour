from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserFollowerViewSet, TagViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'followers', UserFollowerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# GET /posts/ - 獲取所有貼文。
# POST /posts/ - 新增貼文。
# PUT /posts/{id}/ - 修改貼文。
# GET /posts/homepage/ - 獲取首頁貼文。
# GET /posts/user_page/ - 獲取個人頁面的貼文。
# POST /posts/{id}/bookmark/ - 收藏貼文。
# POST /posts/{id}/add_comment/ - 新增留言。
# GET /followers/ - 獲取所有追蹤資料。
# GET /followers/follow_overview/ - 追蹤總覽。

