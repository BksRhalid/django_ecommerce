#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
<<<<<<< HEAD
                          'djecommerce.settings.production')
=======
                          'djecommerce.settings.production')  # djecommerce.settings.development
>>>>>>> f43a2d3e56d0dbbb07290cc65dd55356ba155901
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
