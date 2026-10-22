import pytest
from django.apps import apps
from django.db.models.query import QuerySet
from django.test import override_settings

from .models import BulkTestModel


def patched_methods():
    return QuerySet.bulk_create, QuerySet.bulk_update, QuerySet.update


def test_ready_is_idempotent():
    before = patched_methods()

    apps.get_app_config("bulk_signals").ready()

    assert patched_methods() == before


@pytest.mark.django_db
def test_skip_signal_survives_app_registry_reload(mocker, settings):
    create_stub = mocker.patch("tests.models.create_stub")

    with override_settings(INSTALLED_APPS=list(settings.INSTALLED_APPS)):
        BulkTestModel.objects.bulk_create([BulkTestModel()], skip_signal=True)

    assert create_stub.call_count == 0
