![Testing](https://github.com/awmath/django-bulk-signals/actions/workflows/ci.yaml/badge.svg)
[![CodeFactor](https://www.codefactor.io/repository/github/awmath/django-bulk-signals/badge)](https://www.codefactor.io/repository/github/awmath/django-bulk-signals)
[![codecov](https://codecov.io/gh/awmath/django-bulk-signals/branch/main/graph/badge.svg?token=aaYFGNAvqM)](https://codecov.io/gh/awmath/django-bulk-signals)
# django-bulk-signals
signals for usage with django bulk queryset methods

# usage
Add app to settings
```
INSTALLED_APPS = [
    ...,
    bulk_signals,
    ...
]
```
Import signals and connect.

```
from django.dispatch import receiver
from bulk_signals import signals

@receiver(signals.post_bulk_update, signals.post_bulk_update, signals.post_query_update)
def debug(*args, **kwargs):
    print(args)
    print(kwargs)
```

# TODO
-  pre_*** signals
-  test against different database backends
