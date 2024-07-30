from django.urls import path
from line.views import callback

urlpatterns = [
    path("callback", callback, name='line_callback'),
]
