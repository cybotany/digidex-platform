from django.apps import AppConfig


class LinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digidex.link'

    def ready(self):
        import digidex.link.signals
