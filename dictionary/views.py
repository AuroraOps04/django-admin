from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from dictionary.serializers import DictionaryItemSerializer, DictionarySerializer
from dictionary.models import Dictionary, DictionaryItem


# Create your views here.

class DictionaryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    @action(detail=False, methods=['get'])
    def by_type(self, request):
        if not request.GET['type']:
            raise ValidationError("type 参数必传")
        dictionary = Dictionary.objects.prefetch_related("items").filter(type=request.GET['type']).first()
        if not dictionary:
            raise ValidationError("type 不存在")
        return Response({
            "type": dictionary.type,
            "id": dictionary.id,
            "name": dictionary.name,
            "status": dictionary.status,
            "items": DictionaryItemSerializer(dictionary.items, many=True).data,
        })

class DictionaryItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = DictionaryItem.objects.all()
    serializer_class = DictionaryItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
