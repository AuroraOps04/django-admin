from rest_framework import serializers

from dictionary.models import DictionaryItem,Dictionary




class DictionaryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DictionaryItem
        fields = ['id', 'status', 'dictionary', 'sort', 'label', 'value', 'is_default', 'css_class', 'list_class']

class DictionarySerializer(serializers.ModelSerializer):
    items = DictionaryItemSerializer(many=True, read_only=True)
    class Meta:
        model = Dictionary
        fields = ['id', 'status', 'name', 'type', 'items']