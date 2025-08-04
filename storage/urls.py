from django.urls import path, include
from rest_framework.routers import DefaultRouter

from storage.views import  UploadFileViewSet

router = DefaultRouter()
router.register("file", UploadFileViewSet)
urlpatterns = [
    path("", include(router.urls))
]