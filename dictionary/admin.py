from django.contrib import admin

from dictionary.models import DictionaryItem, Dictionary

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(DictionaryItem)