from django.urls import path
from .views import CustomGoogleLogin, CustomLineLogin

urlpatterns = [
    path('login/google/', CustomGoogleLogin.as_view(), name='google_login'),
    path('login/line/', CustomLineLogin.as_view(), name='line_login'),
]