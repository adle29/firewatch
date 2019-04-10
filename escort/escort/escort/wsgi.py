"""
WSGI config for escort project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEV = True

if DEV: #os.environ.get('DJANGO_DEVELOPMENT') is not None:
    print("DEBUG MODE")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "escort.settings_dev")
else:
    print("PRODUCTION MODE")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "escort.settings")

application = get_wsgi_application()
