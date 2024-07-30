from django.urls import path
from .views import GoogleLogin, LineLogin, GoogleLoginCallback, LineLoginCallback

urlpatterns = [
  path('google/login/', GoogleLogin.as_view(), name='google_login'),
  path('line/login/', LineLogin.as_view(), name='line_login'),
  path('google/callback/', GoogleLoginCallback.as_view(), name='google_callback'),
  path('line/callback/', LineLoginCallback.as_view(), name='line_callback'),
]
