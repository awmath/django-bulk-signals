from django.apps import AppConfig


class BuildingTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests"
    label = "bulk_signals_test"
