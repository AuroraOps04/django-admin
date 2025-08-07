from rest_framework import serializers
from menu.models import Menu, MenuMeta


class MenuMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMeta
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
