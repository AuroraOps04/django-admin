from django.contrib import admin

from menu.models import Menu, MenuMeta

# Register your models here.

# admin.site.register(Menu)
# admin.site.register(MenuMeta)


class MenuMetaInline(admin.StackedInline):
    model = MenuMeta
    can_delete = False


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuMetaInline]
