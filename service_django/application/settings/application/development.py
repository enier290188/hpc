from django.utils.translation import ugettext_lazy as _
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')[1:-1]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Allowed hosts
ALLOWED_HOSTS = ['*']

# WSGI
WSGI_APPLICATION = 'wsgi.application.wsgi.application'

# Root url
ROOT_URLCONF = 'src.application.urls_%s' % (os.environ.get('APPLICATION_ENVIRONMENT'),)

# Installed applications
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'django.contrib.auth',
    'django.contrib.admin',
    'captcha',
    'src.application.security',
    'src.application.help',
    'src.application.website',
    'src.application.hpc',
    'src.application.bigdata',
    'src.application.administration',
]

# Middleware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'src.application.security.middleware.ApplicationSecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Havana'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# List of languages used
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

# Directory that will host po and mo files
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'i18n/application/security/locale/application___security/locale'),
    #
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website/locale'),
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website___header/locale'),
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website___leftside/locale'),
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website___content/locale'),
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website___content___website_home/locale'),
    os.path.join(BASE_DIR, 'i18n/application/website/locale/application___website___content___website_help/locale'),
    #
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___header/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___leftside/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___content/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___content___hpc_jobs/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___content___hpc_script/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___content___hpc_nodes/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___content___hpc_explorer/locale'),
    os.path.join(BASE_DIR, 'i18n/application/hpc/locale/application___hpc___ssh/locale'),
    #
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___header/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___leftside/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___content/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___content___bigdata_module01/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___content___bigdata_module02/locale'),
    os.path.join(BASE_DIR, 'i18n/application/bigdata/locale/application___bigdata___content___bigdata_module03/locale'),
    #
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___header/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___leftside/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___localuser/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___localuserrequest/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___ldapuser/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___ldapuserrequest/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___ldapuserimported/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___group/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_security___permission/locale'),
    os.path.join(BASE_DIR, 'i18n/application/administration/locale/application___administration___content___admin_help___document/locale'),
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'volumes', 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'volumes', 'mediafiles')

# Emails settings
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST')[1:-1]
EMAIL_PORT = int(os.environ.get('DJANGO_EMAIL_PORT')[1:-1])
EMAIL_USER_NOREPLY = os.environ.get('DJANGO_EMAIL_USER_NOREPLY')[1:-1]

# LDAP settings
LDAP_SERVER_HOST = os.environ.get('DJANGO_LDAP_SERVER_HOST')[1:-1]
LDAP_SERVER_PORT = int(os.environ.get('DJANGO_LDAP_SERVER_PORT')[1:-1])
LDAP_SERVER_USER = os.environ.get('DJANGO_LDAP_SERVER_USER')[1:-1]
LDAP_SERVER_PASSWORD = os.environ.get('DJANGO_LDAP_SERVER_PASSWORD')[1:-1]
LDAP_SERVER_GROUPS_SEARCH_BASE = os.environ.get('DJANGO_LDAP_SERVER_GROUPS_SEARCH_BASE')[1:-1]
LDAP_SERVER_GROUPS_LIST = os.environ.get('DJANGO_LDAP_SERVER_GROUPS_LIST')[1:-1].split()
LDAP_SERVER_GROUPS_GROUP_CN = os.environ.get('DJANGO_LDAP_SERVER_GROUPS_GROUP_CN')[1:-1]
LDAP_SERVER_GROUPS_GROUP_GIDNUMBER = os.environ.get('DJANGO_LDAP_SERVER_GROUPS_GROUP_GIDNUMBER')[1:-1]
LDAP_SERVER_USERS_SEARCH_BASE = os.environ.get('DJANGO_LDAP_SERVER_USERS_SEARCH_BASE')[1:-1]
LDAP_SERVER_USERS_HPC_SEARCH_BASE = os.environ.get('DJANGO_LDAP_SERVER_USERS_HPC_SEARCH_BASE')[1:-1]
LDAP_SERVER_USERS_HOMEDIRECTORY = os.environ.get('DJANGO_LDAP_SERVER_USERS_HOMEDIRECTORY')[1:-1]

# CLUSTER settings
CLUSTER_SERVER_HOST = os.environ.get('DJANGO_CLUSTER_SERVER_HOST')[1:-1]
CLUSTER_SERVER_PORT = int(os.environ.get('DJANGO_CLUSTER_SERVER_PORT')[1:-1])

# Celery settings
CELERY_BROKER_URL = 'amqp://%s:%s@%s:%s//' % (os.environ.get('RABBITMQ_DEFAULT_USER'), os.environ.get('RABBITMQ_DEFAULT_PASS'), os.environ.get('RABBITMQ_HOST'), os.environ.get('RABBITMQ_PORT'),)
CELERY_RESULT_BACKEND = 'django-db'
