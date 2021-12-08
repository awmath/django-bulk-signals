from django import dispatch

from django.dispatch import receiver, Signal

post_bulk_create = Signal()
post_bulk_update = Signal()
post_query_update = Signal()
