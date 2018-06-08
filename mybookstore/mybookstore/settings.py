"""
Django settings for mybookstore project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't*m1shi_+9_bpgu@okvw+++czf(h@i11y&dj@28n_u##17jg)4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'books',
    'tinymce',  # 富文本编辑器
    'cart',
    'order',
    'comments',
    'haystack',  # 全文搜索
    'users.templatetags.filters'  # 过滤器功能
)
# 富文本编辑器*******************************************
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
# *****************************************************
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'utils.middleware.BookMiddleware',
    'utils.middleware.AnotherMiddleware',
    'utils.middleware.UrlPathRecordMiddleware',
    'utils.middleware.BlockedIpMiddleware',
)

ROOT_URLCONF = 'mybookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mybookstore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'fenglei',
    }
}

#  引入redis session缓存***************************************
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # 默认存在redis第一个数据库
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': ''
        }
    }
}
# session引擎************************************************
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内置缓存,此处别名依赖缓存的设置）

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# 配置静态文件************************************************
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')

# 支付宝支付**************************************************
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'

# 全文检索配置 **********************************************
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎, 支持中文搜索
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6  # 指定搜索结果每页的条数

# 邮件配置*************************************************
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
# 126和163邮箱的SMTP端口为25,QQ邮箱端口为465
EMAIL_PORT = 25
# 如果使用QQ邮箱发送邮件，需要开启SSL加密, 如果在aliyun上部署，也需要开启ssl加密，同时修改端口为EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# 发送邮件的邮箱, 必须真实可用
EMAIL_HOST_USER = '17515755669@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'atguigu'
# 收件人看到的发件人
EMAIL_FROM = 'shangguigu<17515755669@163.com>'

# 记录日志***************************************************
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {             # 日志输出的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {               # 处理日志的函数
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/log/debug.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
        },
        'django.request': {     # 日志的命名空间
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}