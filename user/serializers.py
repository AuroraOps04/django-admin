from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import UserDetail
from django.contrib.auth import get_user, get_user_model


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source="user.password", write_only=True)
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = UserDetail
        fields = ["username", "email", "nickname", "avatar", "password"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        # 注意是 create_user 如果是普通的 create 方法，不会自动调用加密密码的方法
        user = get_user_model().objects.create_user(**user_data)
        detail = UserDetail.objects.create(user=user, **validated_data)
        return detail

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     return token
    def validate(self, attrs):
        data = super().validate(attrs)
        data['accessToken'] = data['access']
        return data