from rest_framework import routers
from django.urls import path, include
from dictionary.views import DictionaryItemViewSet,DictionaryViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register('dict', DictionaryViewSet)
# item_router = routers.NestedSimpleRouter(router, 'dict', lookup='dictionary')
router.register('dict_item', DictionaryItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]