from django.urls import path, include
from outfit_scheduler import views

from rest_framework.routers import DefaultRouter
from .views import OutfitScheduleViewSet, EventLogsViewSet

router = DefaultRouter()
router.register(r'schedule', OutfitScheduleViewSet)
router.register(r'event-logs', EventLogsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# GET /schedule/ - 獲取所有行程安排。
# POST /schedule/add_event/ - 新增穿搭行程活動。
# GET /schedule/calendar/ - 顯示行事曆中的所有活動。
# GET /event-logs/ - 獲取所有活動日誌。
# GET /event-logs/{id}/ - 獲取指定活動日誌。

