"""
WSGI config for DjangoRestAPI4thHW project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoRestAPI4thHW.settings')

application = get_wsgi_application()

# Vercel requires the callable to be named 'app' or 'handler'
app = application
handler = application
