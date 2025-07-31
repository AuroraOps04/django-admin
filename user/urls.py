from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import LoginView, RegisterView, UserInfoView, LoginUserPermissionsView, LogoutView

router = DefaultRouter()

# router.register("auth/login", LoginView)


urlpatterns = [
    path("auth/login", LoginView.as_view()),
    path("auth/logout", LogoutView.as_view()),
    path("auth/refresh", TokenRefreshView.as_view()),
    path("auth/codes", LoginUserPermissionsView.as_view()),
    path("register", RegisterView.as_view()),
    path("user/info", UserInfoView.as_view()),

]
