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

# Initialize Django
application = get_wsgi_application()

# Run migrations and create sample data on startup
try:
    from django.core.management import call_command
    call_command('migrate', verbosity=0, interactive=False)
    call_command('populate_data', verbosity=0)
except Exception as e:
    print(f"Database initialization error: {e}")
    pass
