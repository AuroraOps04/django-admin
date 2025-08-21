from django.contrib.auth import get_user_model, logout
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from user.filters import UserFilter
from user.models import Role
from user.serializers import (
    CustomTokenObtainPairSerializer,
    RoleSerializer,
    UserSerializer,
)

# Create your views here.

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # TODO: 给注册的用户默认角色
        return super().perform_create(serializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    ordering = ("-date_joined",)
    filterset_class = UserFilter
    ordering_fields = ("date_joined", "id")

    @action(detail=False, methods=["get"])
    def info(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # 这个其实没啥用,在 jwt 模式
        logout(request)
        return Response()


class LoginUserPermissionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        perms = request.user.get_all_permissions()
        return Response(perms)


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
