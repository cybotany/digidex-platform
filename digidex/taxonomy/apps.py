from django.apps import AppConfig


class TaxonomyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digidex.taxonomy'

    def ready(self):
            import digidex.taxonomy.signals