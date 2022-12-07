# -*- coding: utf-8 -*-
from django.apps import AppConfig, apps

from bulk_signals import signals


class BulkSignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bulk_signals"

    def ready(self):
        # monkey patch bulk method handling into the queryset
        from django.db.models.query import QuerySet

        base_bulk_create = QuerySet.bulk_create

        def bulk_create(queryset, objects, **kwargs):
            # get model label from queryset
            model = apps.get_model(queryset.model._meta.label)

            signals.pre_bulk_create.send(sender=model, objects=objects, **kwargs)
            created_objects = base_bulk_create(queryset, objects, **kwargs)
            signals.post_bulk_create.send(sender=model, objects=objects, **kwargs)

            return created_objects

        QuerySet.bulk_create = bulk_create

        base_bulk_update = QuerySet.bulk_update

        def bulk_update(queryset, objects, fields, **kwargs):
            queryset._hints["is_bulk_update"] = True
            model = apps.get_model(queryset.model._meta.label)

            signals.pre_bulk_update.send(
                sender=model, objects=objects, fields=fields, **kwargs
            )
            return_value = base_bulk_update(queryset, objects, fields, **kwargs)
            signals.post_bulk_update.send(
                sender=model, objects=objects, fields=fields, **kwargs
            )

            return return_value

        QuerySet.bulk_update = bulk_update

        base_update = QuerySet.update

        def update(queryset, **kwargs):
            model = apps.get_model(queryset.model._meta.label)

            # if this update is part of a bulk_update action skip this part
            if queryset._hints.get("is_bulk_update", False):
                return base_update(queryset, **kwargs)

            signals.pre_query_update.send(
                sender=model, queryset=queryset, update_kwargs=kwargs
            )
            return_val = base_update(queryset, **kwargs)
            signals.post_query_update.send(
                sender=model, queryset=queryset, update_kwargs=kwargs
            )

            return return_val

        QuerySet.update = update
