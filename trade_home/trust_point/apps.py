from django.apps import AppConfig


class TrustPointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trust_point'

    def ready(self):
        import trust_point.signal
