from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from menu.serializers import AllMenuSerializer, MenuSerializer, TreeMenuSerializer
from menu.models import Menu

# Create your views here.


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def all(self, request):
        # TODO: 根据角色获取路由
        items = (
            Menu.objects.prefetch_related("children")
            .filter(parent__isnull=True, status=True)
            .exclude(type="button")
            .order_by("meta__order")
            .all()
        )
        serializer = AllMenuSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def tree(self, request):
        items = Menu.objects.filter(parent__isnull=True).order_by("meta__order").all()
        serializer = TreeMenuSerializer(items, many=True)
        return Response(serializer.data)
