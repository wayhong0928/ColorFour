from django.contrib import admin
from django.urls import include, path



urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('djoser.urls')),
	path('api/', include('djoser.urls.authtoken')),
	path('accounts/', include('allauth.urls')),
	# path('color/', include('color_analyzer.urls')),
	path('wardrobe/', include('wardrobe_manager.urls')),
	# path('recommender/', include('outfit_recommender.urls')),
	# path('social/', include('social_platform.urls')),
	# path('shopping/', include('shopping_advisor.urls')),
	# path('outfit/', include('outfit_scheduler.urls')),
	path('line/', include('line.urls')),
]
