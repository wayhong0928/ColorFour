from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserColorTestViewSet

router = DefaultRouter()
router.register(r'user-tests', UserColorTestViewSet, basename='usercolortest')

urlpatterns = [
    path('', include(router.urls)),
]
