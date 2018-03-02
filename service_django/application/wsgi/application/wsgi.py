import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.application.%s' % (os.environ.get('APPLICATION_ENVIRONMENT'),))
application = get_wsgi_application()
