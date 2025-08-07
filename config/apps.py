from django.apps import AppConfig


def _add_item(d, field, value):
    if field in d:
        d[field].append(value)
    else:
        d[field] = [value]


class ConfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "config"

    def ready(self):
        from django.conf import settings
        from rest_framework.settings import api_settings

        if not hasattr(settings, "REST_FRAMEWORK"):
            settings.REST_FRAMEWORK = {}
        api_style = None if not hasattr(settings, "API_STYLE") else settings.API_STYLE
        if api_style == "Vben":
            _add_item(
                settings.REST_FRAMEWORK,
                "DEFAULT_RENDERER_CLASSES",
                "config.renderers.VbenJsonRenderer",
            )
            settings.REST_FRAMEWORK["EXCEPTION_HANDLER"] = (
                "config.exceptions.vben_exception_handler"
            )
            settings.REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
                "config.paginations.VbenPagination"
            )
        elif api_style is None:
            _add_item(
                settings.REST_FRAMEWORK,
                "DEFAULT_RENDERER_CLASSES",
                "config.renderers.VbenJsonRenderer",
            )
            settings.REST_FRAMEWORK["EXCEPTION_HANDLER"] = (
                "config.exceptions.vben_exception_handler"
            )
            settings.REST_FRAMEWORK["DEFAULT_PAGINATION_CLASS"] = (
                "config.paginations.VbenPagination"
            )
        # 确保 DRF　重新加载配置
        api_settings.reload()
