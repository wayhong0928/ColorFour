from django.urls import path
from line.views import callback
from . import views

urlpatterns = [
    path("callback", callback, name='line_callback'),
    path('login', views.line_login, name='line_login'),
]
