from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digit.accounts'

    def ready(self):
        import digit.accounts.signals
