import pytest

from .models import BulkTestModel

pytestmark = pytest.mark.django_db


@pytest.fixture(params=[True, False])
def skip(request):
    return request.param


def test_bulk_create(mocker, skip):
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")

    BulkTestModel.objects.bulk_create(
        [BulkTestModel() for _ in range(10)], skip_signal=skip
    )

    assert create_stub.call_count == 0 if skip else 1


def test_bulk_update(mocker, objects, skip):
    bulk_update_stub = mocker.patch("bulk_signals.tests.models.update_stub")

    BulkTestModel.objects.bulk_update(objects, ["num"], skip_signal=skip)

    assert bulk_update_stub.call_count == 0 if skip else 1


def test_update(mocker, objects, skip):
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    BulkTestModel.objects.update(num=1, skip_signal=skip)

    assert update_stub.call_count == 0 if skip else 2


def test_custom_key(mocker, skip, settings):
    settings.BULK_SIGNALS_SKIP_KEY = "different"
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")

    BulkTestModel.objects.bulk_create(
        [BulkTestModel() for _ in range(10)], different=skip
    )

    assert create_stub.call_count == 0 if skip else 1
