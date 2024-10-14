from django.urls import path, include
from .views import add_color_analysis, DeleteColorAnalysisView, UserColorTestsViewSet, ColorTestQuestionsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user-tests', UserColorTestsViewSet)
router.register(r'questions', ColorTestQuestionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', add_color_analysis, name='add_color_analysis'),
    path('delete/<int:item_id>/', DeleteColorAnalysisView.as_view(), name='delete_color_analysis'),
]

# GET /user-tests/ - 獲取所有用戶的色彩測驗結果。
# GET /user-tests/{id}/result/ - 獲取指定用戶的色彩測驗結果。
# POST /user-tests/{id}/retake_test/ - 重新測驗指定用戶的色彩分析。
# GET /questions/ - 獲取所有色彩測驗的問題。
# POST /add/ - 新增色彩分析記錄。
# DELETE /delete/{item_id}/ - 刪除色彩分析資料。
