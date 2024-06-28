from django.apps import AppConfig


class AssetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'asset'

    def ready(self):
        import asset.signals
