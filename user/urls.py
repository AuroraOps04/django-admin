from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import (
    LoginView,
    RegisterView,
    LoginUserPermissionsView,
    LogoutView,
    UserViewSet,
    RoleViewSet,
)

router = DefaultRouter(trailing_slash=False)

router.register("user", UserViewSet)
router.register("role", RoleViewSet)

urlpatterns = [
    path("auth/login", LoginView.as_view()),
    path("auth/logout", LogoutView.as_view()),
    path("auth/refresh", TokenRefreshView.as_view()),
    path("auth/codes", LoginUserPermissionsView.as_view()),
    path("register", RegisterView.as_view()),
    path("", include(router.urls)),
]
