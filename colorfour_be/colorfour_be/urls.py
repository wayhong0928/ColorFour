from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from member.views import CustomGoogleLogin, CustomLineLogin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/google/", CustomGoogleLogin.as_view(), name="google_login"),
    path("dj-rest-auth/line/", CustomLineLogin.as_view(), name="line_login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("member/", include("member.urls")),
    path("color/", include("color_analyzer.urls")),
    path("wardrobe/", include("wardrobe_manager.urls")),
    path("recommender/", include("outfit_recommender.urls")),
    path("social/", include("social_platform.urls")),
    path("shopping/", include("shopping_advisor.urls")),
    path("outfit/", include("outfit_scheduler.urls")),
    path("line/", include("line.urls")),

    path('social_platform/', include('social_platform.urls')),  # 留言功能
]
