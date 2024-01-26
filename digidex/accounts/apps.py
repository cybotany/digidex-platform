from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digidex.accounts'

    def ready(self):
        import digidex.accounts.signals
