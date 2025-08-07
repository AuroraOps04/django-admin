from django.shortcuts import render
from rest_framework import viewsets, permissions

from menu.serializers import MenuSerializer
from menu.models import Menu

# Create your views here.


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]
