import os
import environ

# ======================= BASE ===============================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# ======================= ENV ================================================
env = environ.Env(
    DEBUG=(bool, False),
    APP_INSTANCE=(str, 'dev'),
)

if os.path.isfile(os.path.join(BASE_DIR, 'project', 'settings', '.env')):
    environ.Env.read_env(os.path.join(BASE_DIR, 'project', 'settings', '.env'))

DEBUG = env('DEBUG')
APP_INSTANCE = env('APP_INSTANCE')

# ======================= TELEGRAM BOT ===========================================
BOT_API_KEY = env('BOT_API_KEY', default='')
BOT_CHAT_ID = env('BOT_CHAT_ID', default='')

# ======================= SECURITY ===========================================
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY', default='y$o97r*90ixip94186+%_7&2o018hlyvd8n3hzecf6gyirnd4r')

# ======================= APPLICATIONS =======================================
INSTALLED_APPS = [
    'applications.app.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'adminsortable2',
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
    'easy_thumbnails.optimize',

    'applications.banners',
    'applications.channels',
    'applications.core',
    'applications.handbook',
    'applications.maps',
    'applications.news',
    'applications.promotions',
    'applications.tariffs',
    'applications.tbot',
]

# ======================= MIDDLEWARE =========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'applications.core.middleware.CityMiddleware',
]

# ======================= URLS ===============================================
ROOT_URLCONF = 'project.urls'

# ======================= TEMPLATES ==========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'applications.core.context_processors.global_settings',
            ],
        },
    },
]

# ======================= USGI ===============================================
WSGI_APPLICATION = 'project.wsgi.application'

# ======================= DATABASES ==========================================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env('POSTGRES_DB', default='neotv'),
#         'USER': env('POSTGRES_USER', default='root'),
#         'PASSWORD': env('POSTGRES_PASSWORD', default='root'),
#         'HOST': env('POSTGRES_HOST', default='127.0.0.1'),
#         'PORT': env('POSTGRES_PORT', default=5432),
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# ======================= LOCALE =============================================
LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ======================= STATIC =============================================
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles/dst/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# ======================= MEDIA =============================================
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# ======================= SENTRY =========================================
SENTRY_URL = 'https://sentry.io/api/embed/error-page/'

# ======================= LOGGING ================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'propagate': False,
        },
    }
}

# ======================= PROJECT =========================================
BANNER_RESOLUTION = '1440x320'
DEFAULT_CITY = 1
DEFAULT_CITY_TITLE = 'Бишкек'

# ======================= THUMBNAIL =========================================
THUMBNAIL_ALIASES = {
    '': {
        'banner': {'size': (1440, 320), 'crop': None},
        'channel': {'size': (80, 80), 'crop': None},
        'promotions': {'size': (450, 225), 'crop': 'scale'},
        'promotion_details': {'size': (700, 350), 'crop': 'smart'},
    },
}

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}'
}

# ======================= CKEDITOR =========================================
CKEDITOR_UPLOAD_PATH = 'uploads/'
