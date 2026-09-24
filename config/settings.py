import os
from pathlib import Path
from urllib.parse import urlparse

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


# =========================
# SECURITY
# =========================

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'dev-only-change-this-key'
)

DEBUG = os.getenv(
    'DEBUG',
    'True'
).lower() in {'1', 'true', 'yes'}


# =========================
# ALLOWED HOSTS
# =========================

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'euonusitbackend-production.up.railway.app',
]


# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [
    'corsheaders',
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'website',
]


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URL / WSGI
# =========================

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================
# DATABASE
# =========================

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'sqlite:///db.sqlite3'
)

if DATABASE_URL.startswith(('postgres://', 'postgresql://')):

    parsed = urlparse(DATABASE_URL)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': parsed.path.lstrip('/'),
            'USER': parsed.username or '',
            'PASSWORD': parsed.password or '',
            'HOST': parsed.hostname or '',
            'PORT': str(parsed.port or 5432),
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = []


# =========================
# LANGUAGE / TIMEZONE
# =========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# =========================
# STATIC FILES
# =========================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },

    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# =========================
# MEDIA FILES
# =========================

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# DEFAULT PRIMARY KEY
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# CORS
# =========================

CORS_ALLOWED_ORIGINS = [
    'https://euonus-it.vercel.app',
    'https://euonus-it-ynbx.vercel.app',
    'http://localhost:5173',
    'http://localhost:5174',
]

CSRF_TRUSTED_ORIGINS = [
    'https://euonus-it.vercel.app',
    'https://euonus-it-ynbx.vercel.app',
    'https://euonusitbackend-production.up.railway.app',
]


# =========================
# DJANGO REST FRAMEWORK
# =========================

# =========================
# JAZZMIN ADMIN THEME
# =========================
JAZZMIN_SETTINGS = {
    'site_title': 'Euonus IT Admin',
    'site_header': 'Euonus IT',
    'site_brand': 'Euonus IT',
    'welcome_sign': 'Welcome to Euonus IT Admin',
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    'order_with_respect_to': ['website', 'auth'],
    'icons': {
        'website.service': 'fas fa-cogs',
        'website.project': 'fas fa-briefcase',
        'website.blog': 'fas fa-newspaper',
        'website.contact': 'fas fa-envelope',
        'website.jobopening': 'fas fa-user-tie',
        'website.company': 'fas fa-building',
        'website.client': 'fas fa-users',
    },
}

JAZZMIN_UI_TWEAKS = {
    'theme': 'darkly',
    'dark_mode_theme': 'darkly',
    'light_mode_theme': 'flatly',
    'navbar': 'navbar-dark bg-primary',
    'sidebar': 'sidebar-dark-primary',
    'brand_colour': 'navbar-primary',
    'accent': '#2c7be5',
    'show_ui_builder': False,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ],
}
