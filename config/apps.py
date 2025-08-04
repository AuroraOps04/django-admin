from django.apps import AppConfig


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
            settings.REST_FRAMEWORK.setdefault(
                "DEFAULT_RENDERER_CLASSES", ["config.renderers.VbenJsonRenderer"]
            )
            settings.REST_FRAMEWORK.setdefault(
                "EXCEPTION_HANDLER",
                "config.exceptions.vben_exception_handler",
            )
            settings.REST_FRAMEWORK.setdefault(
                "DEFAULT_PAGINATION_CLASS", "config.paginations.VbenPagination"
            )
        elif api_style is None:
            settings.REST_FRAMEWORK.setdefault(
                "DEFAULT_RENDERER_CLASSES", ["config.renderers.VbenJsonRenderer"]
            )
            settings.REST_FRAMEWORK.setdefault(
                "DEFAULT_PAGINATION_CLASS", "config.paginations.VbenPagination"
            )
            settings.REST_FRAMEWORK.setdefault(
                "EXCEPTION_HANDLER",
                "config.exceptions.vben_exception_handler",
            )
        # 确保 DRF　重新加载配置
        api_settings.reload()
