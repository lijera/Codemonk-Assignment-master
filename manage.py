#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the default Django settings module to 'codemonk.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codemonk.settings')
    try:
        # Import execute_from_command_line function from Django's management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or not available, raise ImportError with instructions
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# If this script is run directly, execute the main function
if __name__ == '__main__':
    main()
