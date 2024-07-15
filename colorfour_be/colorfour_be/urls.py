from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    # path('api/', include('color_analyzer.urls')),
    # path('api/', include('wardrobe_manager.urls')),
    # path('api/', include('outfit_recommender.urls')),
    # path('api/', include('social_platform.urls')),
    # path('api/', include('shopping_advisor.urls')),
    # path('api/', include('outfit_scheduler.urls')),
    path('line/', include('line.urls')),
    path('accounts/', include('allauth.urls')),

]
