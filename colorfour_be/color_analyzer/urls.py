from django.urls import path
from .views import add_color_analysis, DeleteColorAnalysisView


urlpatterns = [
    path('add/', add_color_analysis, name='add_color_analysis'),
    path('delete/<int:item_id>/', DeleteColorAnalysisView.as_view(), name='delete_color_analysis'),
]
