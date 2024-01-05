from django.apps import AppConfig, apps
from django.conf import settings

from bulk_signals import signals


def skip_signal(kwargs):
    skip_key = getattr(settings, "BULK_SIGNALS_SKIP_KEY", "skip_signal")
    return kwargs.pop(skip_key, False) is True


class BulkSignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bulk_signals"

    def ready(self):
        # monkey patch bulk method handling into the queryset
        from django.db.models.query import QuerySet

        base_bulk_create = QuerySet.bulk_create

        def bulk_create(queryset, objs, **kwargs):
            if skip_signal(kwargs):
                return base_bulk_create(queryset, objs, **kwargs)
            # get model label from queryset
            model = apps.get_model(queryset.model._meta.label)

            signals.pre_bulk_create.send(sender=model, objects=objs, **kwargs)
            created_objects = base_bulk_create(queryset, objs, **kwargs)
            signals.post_bulk_create.send(sender=model, objects=objs, **kwargs)

            return created_objects

        QuerySet.bulk_create = bulk_create

        base_bulk_update = QuerySet.bulk_update

        def bulk_update(queryset, objs, fields, **kwargs):
            # add a queryset hint so update signals won't be
            # triggerd for bulk_update
            queryset._hints["is_bulk_update"] = True

            # check if the signals should be skipped
            if skip_signal(kwargs):
                return base_bulk_update(queryset, objs, fields, **kwargs)

            model = apps.get_model(queryset.model._meta.label)

            signals.pre_bulk_update.send(
                sender=model, objects=objs, fields=fields, **kwargs
            )
            return_value = base_bulk_update(queryset, objs, fields, **kwargs)
            signals.post_bulk_update.send(
                sender=model, objects=objs, fields=fields, **kwargs
            )

            return return_value

        QuerySet.bulk_update = bulk_update

        base_update = QuerySet.update

        def update(queryset, **kwargs):
            # check if the signals should be skipped
            if skip_signal(kwargs):
                return base_update(queryset, **kwargs)

            model = apps.get_model(queryset.model._meta.label)

            # if this update is part of a bulk_update action skip this part
            if queryset._hints.get("is_bulk_update", False):
                return base_update(queryset, **kwargs)

            signals.pre_query_update.send(
                sender=model, queryset=queryset, update_kwargs=kwargs
            )
            return_val = base_update(queryset, **kwargs)
            signals.post_query_update.send(
                sender=model,
                queryset=queryset,
                update_kwargs=kwargs,
                update_count=return_val,
            )

            return return_val

        QuerySet.update = update
