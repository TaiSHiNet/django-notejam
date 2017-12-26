import os

APP_ENV = os.environ.get("APP_ENV")

from settings_dev import *  # noqa

if APP_ENV == 'production':
    from settings_prod import *  # noqa
