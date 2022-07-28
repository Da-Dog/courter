from django.urls import re_path, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from . import views

router = DefaultRouter()
router.register(r'players', views.AdminPlayerViewset)
router.register(r'courts', views.AdminCourtViewset)

urlpatterns = [
    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls
