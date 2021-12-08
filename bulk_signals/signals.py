# -*- coding: utf-8 -*-
from django import dispatch
from django.dispatch import Signal, receiver

post_bulk_create = Signal()
post_bulk_update = Signal()
post_query_update = Signal()
