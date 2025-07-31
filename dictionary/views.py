from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins
from dictionary.serializers import DictionaryItemSerializer, DictionarySerializer
from dictionary.models import Dictionary, DictionaryItem


# Create your views here.

class DictionaryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class DictionaryItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = DictionaryItem.objects.all()
    serializer_class = DictionaryItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
