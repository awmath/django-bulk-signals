[![GitHub version](https://badge.fury.io/gh/awmath%2Fdjango-bulk-signals.svg)](https://badge.fury.io/gh/awmath%2Fdjango-bulk-signals)
[![PyPI version](https://badge.fury.io/py/django-bulk-signals.svg)](https://badge.fury.io/py/django-bulk-signals)

![Testing](https://github.com/awmath/django-bulk-signals/actions/workflows/ci.yaml/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/awmath/django-bulk-signals/badge)](https://www.codefactor.io/repository/github/awmath/django-bulk-signals)
[![codecov](https://codecov.io/gh/awmath/django-bulk-signals/branch/main/graph/badge.svg?token=aaYFGNAvqM)](https://codecov.io/gh/awmath/django-bulk-signals)

# Summary
This django library adds signals for the bulk database actions provided by django (`bulk_create`, `bulk_update` and `QuerySet.update`)

# usage
Add app to settings
```
INSTALLED_APPS = [
    ...,
    bulk_signals,
    ...
]
```
Import signals and connect.The signals are connected the same way as in Django itself.
To see them in action use the following snippet:
```
from django.dispatch import receiver
from bulk_signals import signals

@receiver(signals.pre_bulk_update, signals.post_bulk_update, signals.post_query_update)
def debug(*args, **kwargs):
    print(args)
    print(kwargs)
```

You can skip the signals on a single execution by using the `skip_signal=True` keyword argument.
Which keyword should be used for skipping is configurable via the `BULK_SIGNALS_SKIP_KEY="skip_signal"` configuration in the django settings.

# TODO
-  test against different database backends
