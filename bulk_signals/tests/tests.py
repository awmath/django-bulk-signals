# -*- coding: utf-8 -*-
import pytest
from django.db.models import Sum

from .models import BulkTestModel

pytestmark = pytest.mark.django_db


@pytest.fixture
def objects():
    BulkTestModel.objects.bulk_create([BulkTestModel() for _ in range(10)])
    return BulkTestModel.objects.all()


def test_fixture(objects):
    assert BulkTestModel.objects.count() == 10
    assert BulkTestModel.objects.aggregate(sum=Sum("num"))["sum"] == 0


def test_bulk_create(mocker):
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")
    bulk_update_stub = mocker.patch("bulk_signals.tests.models.update_stub")
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    objects = BulkTestModel.objects.bulk_create([BulkTestModel() for _ in range(10)])

    assert bulk_update_stub.call_count == 0
    assert update_stub.call_count == 0
    assert create_stub.call_count == 1


def test_bulk_update(mocker, objects):
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")
    bulk_update_stub = mocker.patch("bulk_signals.tests.models.update_stub")
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    for o in objects:
        o.num = 1

    BulkTestModel.objects.bulk_update(objects, ["num"])

    assert BulkTestModel.objects.aggregate(sum=Sum("num"))["sum"] == 10
    assert bulk_update_stub.call_count == 1
    assert update_stub.call_count == 0
    assert create_stub.call_count == 0


def test_update(mocker, objects):
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")
    bulk_update_stub = mocker.patch("bulk_signals.tests.models.update_stub")
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    BulkTestModel.objects.update(num=1)

    assert BulkTestModel.objects.aggregate(sum=Sum("num"))["sum"] == 10
    assert bulk_update_stub.call_count == 0
    assert update_stub.call_count == 1
    assert create_stub.call_count == 0


def test_no_action(objects, mocker):
    create_stub = mocker.patch("bulk_signals.tests.models.create_stub")
    bulk_update_stub = mocker.patch("bulk_signals.tests.models.update_stub")
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    for o in objects:
        o.num = 1
    BulkTestModel.objects.bulk_update(objects, ["num"], no_action=True)

    BulkTestModel.objects.update(num=2, no_action=True)

    BulkTestModel.objects.bulk_create(
        [BulkTestModel() for _ in range(10)], no_action=True
    )

    assert bulk_update_stub.call_count == 0
    assert update_stub.call_count == 0
    assert create_stub.call_count == 0
