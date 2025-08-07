from django.urls import path, include
from rest_framework.routers import SimpleRouter
from menu.views import MenuViewSet

router = SimpleRouter(trailing_slash=False)

router.register("menu", MenuViewSet)

urlpatterns = [path("", include(router.urls))]
