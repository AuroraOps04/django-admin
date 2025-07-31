from django.contrib.auth import logout
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import UserDetailSerializer, CustomTokenObtainPairSerializer


# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.AllowAny]


class UserInfoView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.detail

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