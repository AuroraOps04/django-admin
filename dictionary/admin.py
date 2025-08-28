from django.contrib import admin

from dictionary.models import DictionaryItem, Dictionary, SysConfig

# Register your models here.

admin.site.register(Dictionary)
admin.site.register(DictionaryItem)
admin.site.register(SysConfig)
