from django.apps import AppConfig


class ZaiappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "zaiapp"

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import zaiapp.signals