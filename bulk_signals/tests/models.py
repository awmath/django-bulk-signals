# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import receiver

from bulk_signals import signals


def create_stub(*args, **kwargs):
    pass


@receiver(signals.post_bulk_create)
def call_create_stub(*args, **kwargs):
    create_stub(*args, **kwargs)


def update_stub(*args, **kwargs):
    pass


@receiver(signals.post_bulk_update)
def call_update_stub(*args, **kwargs):
    update_stub(*args, **kwargs)


def query_update_stub(*args, **kwargs):
    pass


@receiver(signals.pre_query_update)
@receiver(signals.post_query_update)
def call_query_update_stub(*args, **kwargs):
    query_update_stub(*args, **kwargs)


class BulkTestModel(models.Model):
    num = models.IntegerField(default=0)
