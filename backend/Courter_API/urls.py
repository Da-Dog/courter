from django.urls import re_path, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from . import views

router = DefaultRouter()
router.register(r'admin/players', views.AdminPlayerViewset)
router.register(r'admin/courts', views.AdminCourtViewset)

urlpatterns = [
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('players/', views.PlayerView.as_view(), name='players'),
]
urlpatterns += router.urls
