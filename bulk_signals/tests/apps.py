# -*- coding: utf-8 -*-
from django.apps import AppConfig


class BuildingTestConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bulk_signals.tests"
    label = "bulk_signals_test"
