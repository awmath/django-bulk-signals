import pytest
from django.db.models import Sum
from django.dispatch import receiver

from bulk_signals import signals

from .models import BulkTestModel

pytestmark = pytest.mark.django_db


@pytest.fixture()
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

    BulkTestModel.objects.bulk_create([BulkTestModel() for _ in range(10)])

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
    assert update_stub.call_count == 2
    assert create_stub.call_count == 0


def test_pre_bulk_create():
    @receiver(signal=signals.pre_bulk_create)
    def double(sender, objects, *args, **kwargs):
        for o in objects:
            o.num = o.num * 2

    BulkTestModel.objects.bulk_create([BulkTestModel(num=1)])

    assert BulkTestModel.objects.get().num == 2


def test_pre_bulk_update(mocker):
    update_stub = mocker.patch("bulk_signals.tests.models.query_update_stub")

    obj = BulkTestModel.objects.create(num=1)

    obj.num = 2

    @receiver(signal=signals.pre_bulk_update)
    def triple(sender, objects, *args, **kwargs):
        for o in objects:
            o.num = o.num * 3

    BulkTestModel.objects.bulk_update([obj], fields=["num"])

    assert BulkTestModel.objects.get().num == 6
    assert update_stub.call_count == 0


def test_pre_query_update():
    BulkTestModel.objects.create(num=1)

    @receiver(signal=signals.pre_query_update)
    def half(sender, queryset, update_kwargs, **kwargs):
        update_kwargs["num"] /= 2

    BulkTestModel.objects.update(num=8)

    assert BulkTestModel.objects.get().num == 4


def query_update_count_test(*args, **kwargs):
    assert kwargs["update_count"] == 2


def test_query_update_return_count(mocker):
    BulkTestModel.objects.create(num=1)
    BulkTestModel.objects.create(num=1)
    BulkTestModel.objects.create(num=2)

    mocker.patch(
        "bulk_signals.tests.models.query_update_post_stub",
        wraps=query_update_count_test,
    )

    BulkTestModel.objects.filter(num=1).update(num=3)


def test_bulk_signal_arguments():
    BulkTestModel.objects.bulk_create(objs=[])
    BulkTestModel.objects.bulk_update(objs=[], fields=["num"])
