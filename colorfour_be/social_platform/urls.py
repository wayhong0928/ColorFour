from django.urls import path
from social_platform import views
from .views import CommentCreateView

urlpatterns = [
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
]
