from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import UserDetail

User = get_user_model()


# class UserDetailSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(source="user.password", write_only=True)
#     username = serializers.CharField(source="user.username")
#     email = serializers.EmailField(source="user.email")
#
#
#     class Meta:
#         model = UserDetail
#         fields = ["username", "email", "nickname", "avatar", "password"]
#
#     def create(self, validated_data):
#         user_data = validated_data.pop("user")
#         # 注意是 create_user 如果是普通的 create 方法，不会自动调用加密密码的方法
#         user = get_user_model().objects.create_user(**user_data)
#         detail = UserDetail.objects.create(user=user, **validated_data)
#         return detail


class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source="detail.nickname")
    avatar = serializers.ImageField(source="detail.avatar")

    class Meta:
        model = User
        fields = ["nickname", "avatar", "username", "email", "password", "id", "is_active", "date_joined"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    def create(self, validated_data):
        detail = validated_data.pop("detail")
        user = User.objects.create_user(**validated_data)
        UserDetail.objects.create(user=user, **detail)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["accessToken"] = data["access"]
        return data

