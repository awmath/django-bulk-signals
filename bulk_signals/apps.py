# -*- coding: utf-8 -*-
from django.apps import AppConfig, apps
from django.db.models.signals import post_save

from bulk_signals import signals


class BulkSignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bulk_signals"

    def ready(self):
        # monkey patch bulk method handling into the queryset
        from django.db.models.query import QuerySet

        base_bulk_create = QuerySet.bulk_create

        def bulk_create(queryset, objects, **kwargs):
            no_action = kwargs.pop("no_action", False)
            created_objects = base_bulk_create(queryset, objects, **kwargs)
            if no_action:
                return created_objects

            model = apps.get_model(queryset.model._meta.label)
            signals.post_bulk_create.send(sender=model, objects=objects)

            return created_objects

        QuerySet.bulk_create = bulk_create

        base_bulk_update = QuerySet.bulk_update

        def bulk_update(queryset, objects, fields, **kwargs):
            no_action = kwargs.pop("no_action", False)
            queryset._hints["is_bulk_update"] = True
            return_value = base_bulk_update(queryset, objects, fields, **kwargs)
            if no_action:
                return return_value

            model = apps.get_model(queryset.model._meta.label)
            signals.post_bulk_update.send(sender=model, objects=objects)

            return return_value

        QuerySet.bulk_update = bulk_update

        base_update = QuerySet.update

        def update(queryset, **kwargs):
            no_action = kwargs.pop("no_action", False)
            return_val = base_update(queryset, **kwargs)
            # if this update is part of a bulk_update action skip this part
            if no_action or queryset._hints.get("is_bulk_update", False):
                return return_val

            model = apps.get_model(queryset.model._meta.label)
            signals.post_query_update.send(sender=model, queryset=queryset)

            return return_val

        QuerySet.update = update
