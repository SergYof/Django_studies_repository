"""
WSGI config for MyProject_1beta_alpha_prerelease_0dot01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject_1beta_alpha_prerelease_0dot01.settings')

application = get_wsgi_application()
