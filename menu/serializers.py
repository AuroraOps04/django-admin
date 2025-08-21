from rest_framework import serializers
from menu.models import Menu, MenuMeta


class MenuMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMeta
        fields = "__all__"
        extra_kwargs = {"menu": {"read_only": True}}


class MenuSerializer(serializers.ModelSerializer):
    meta = MenuMetaSerializer()

    def create(self, validated_data):
        validated_menu_data = validated_data.pop("meta")

        menu = Menu.objects.create(**validated_data)
        MenuMeta.objects.create(**validated_menu_data, menu=menu)
        return menu

    def update(self, instance, validated_data):
        meta_data = validated_data.pop("meta", None)
        instance = super().update(instance, validated_data)
        if meta_data is not None:
            meta = instance.meta
            if not meta:
                instance.meta = MenuMeta.objects.create(**meta_data)
                instance.save()
            else:
                MenuMetaSerializer().update(meta, meta_data)

        return instance

    class Meta:
        model = Menu
        fields = "__all__"


# for route
class AllMenuSerializer(serializers.ModelSerializer):
    meta = MenuMetaSerializer()
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["id", "name", "meta", "path", "component", "children"]

    def get_children(self, obj):
        items = (
            obj.children.filter(status=True)
            .exclude(type="button")
            .order_by("meta__order")
            .all()
        )
        return TreeMenuSerializer(items, many=True).data


# for tree select
class TreeMenuSerializer(serializers.ModelSerializer):
    meta = MenuMetaSerializer()
    children = serializers.SerializerMethodField()
    type_display = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            "id",
            "name",
            "meta",
            "path",
            "component",
            "children",
            "parent",
            "type",
            "status",
            "type_display",
        ]

    def get_children(self, obj):
        items = obj.children.order_by("meta__order").all()
        return TreeMenuSerializer(items, many=True).data

    def get_type_display(self, obj):
        return obj.get_type_display()
