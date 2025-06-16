"""
WSGI config for DjangoRestAPI4thHW project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoRestAPI4thHW.settings')

# For Vercel deployment, run migrations automatically with in-memory database
if os.environ.get('VERCEL') or ':memory:' in os.environ.get('DATABASE_URL', ''):
    try:
        execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
    except Exception as e:
        print(f"Migration error: {e}")

application = get_wsgi_application()

# Vercel requires the callable to be named 'app' or 'handler'
# Updated: Force new deployment
app = application
handler = application
