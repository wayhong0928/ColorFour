from django.urls import path
from .views import UserAuthProviderView, CustomGoogleLogin, CustomLineLogin

urlpatterns = [
    path('auth-providers/', UserAuthProviderView.as_view(), name='auth_providers'),
    path('login/google/', CustomGoogleLogin.as_view(), name='google_login'),
    path('login/line/', CustomLineLogin.as_view(), name='line_login'),
]