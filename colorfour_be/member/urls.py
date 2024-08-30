from django.urls import path, include
from .views import UserAuthProviderView, BindAnotherLoginProvider

urlpatterns = [
    path('auth-providers/', UserAuthProviderView.as_view(), name='auth_providers'),
    path('bind-provider/', BindAnotherLoginProvider.as_view(), name='bind_provider'),
]
