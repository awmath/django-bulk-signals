# -*- coding: utf-8 -*-
import environ

env = environ.Env()

DEBUG = True
SECRET_KEY = "b76f64b63954cb6b9daff50508a697b4"
ROOT_URLCONF = __name__

INSTALLED_APPS = ["bulk_signals", "bulk_signals.tests"]

urlpatterns = []

DATABASES = {
    "default": env.db_url("SQLITE_URL", default="sqlite:////tmp/my-tmp-sqlite.db"),
}
