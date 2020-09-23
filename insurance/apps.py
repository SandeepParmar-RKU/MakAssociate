from django.apps import AppConfig


class InsuranceConfig(AppConfig):
    name = 'insurance'

    def ready(self):
        import insurance.signals
