from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.authtoken')),
  path('auth/', include('dj_rest_auth.urls')),
  path('auth/social/', include('allauth.socialaccount.urls')),
  path('auth/registration/', include('dj_rest_auth.registration.urls')),
	path('accounts/', include('allauth.urls')),
  path('dj-rest-auth/', include('dj_rest_auth.urls')),
  path('authentication/', include('authentication.urls')),
  
	path('color/', include('color_analyzer.urls')),
	path('wardrobe/', include('wardrobe_manager.urls')),
	path('recommender/', include('outfit_recommender.urls')),
	path('social/', include('social_platform.urls')),
	path('shopping/', include('shopping_advisor.urls')),
	path('outfit/', include('outfit_scheduler.urls')),
	path('line/', include('line.urls')),
]
