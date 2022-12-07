# -*- coding: utf-8 -*-
from django import dispatch
from django.dispatch import Signal, receiver

pre_bulk_create = Signal()
post_bulk_create = Signal()
pre_bulk_update = Signal()
post_bulk_update = Signal()
pre_query_update = Signal()
post_query_update = Signal()
