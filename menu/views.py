from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from menu.serializers import AllMenuSerializer, MenuSerializer
from menu.models import Menu

# Create your views here.


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def all(self, request):
        items = Menu.objects.prefetch_related("children").filter(parent=None).all()
        print(items)
        serializer = AllMenuSerializer(items, many=True)
        return Response(serializer.data)
