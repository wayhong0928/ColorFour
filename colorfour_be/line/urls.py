from django.urls import path
from line.views import callback
from line.views import schedule_event
from . import views

urlpatterns = [
    path("callback", callback, name="line_callback"),
    path("schedule/", schedule_event, name="schedule_event"),
    path("oauth2callback", views.oauth2callback, name="oauth2callback"),
]
