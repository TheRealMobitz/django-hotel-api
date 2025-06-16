import os
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoRestAPI4thHW.settings')
    django.setup()
    
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    
    # Create sample data
    try:
        execute_from_command_line(['manage.py', 'populate_data'])
    except:
        print("Sample data creation skipped")
        pass
