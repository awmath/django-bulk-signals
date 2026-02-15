import pytest

from .models import BulkTestModel


@pytest.fixture()
def objects():
    BulkTestModel.objects.bulk_create([BulkTestModel() for _ in range(10)])
    return BulkTestModel.objects.all()
