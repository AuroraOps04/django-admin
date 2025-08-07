from rest_framework import serializers
from menu.models import Menu, MenuMeta


class MenuMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMeta
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    meta = MenuMetaSerializer()

    def create(self, validated_data):
        validated_menu_data = validated_data.pop("meta")

        menu = Menu.objects.create(**validated_data)
        MenuMeta.objects.create(**validated_menu_data, menu=menu)
        return menu

    class Meta:
        model = Menu
        fields = "__all__"


class AllMenuSerializer(serializers.ModelSerializer):
    meta = MenuMetaSerializer()

    class Meta:
        model = Menu
        fields = ["id", "name", "meta", "path", "component", "children"]
