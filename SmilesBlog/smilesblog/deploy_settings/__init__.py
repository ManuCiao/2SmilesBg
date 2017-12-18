import dj_database_url
from smilesblog.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '.mnsabatino.co.uk',
]

SECRET_KEY = get_env_variable("SECRET_KEY")
NAME_DB = get_env_variable("NAME_DB")
PASSWORD_DB = get_env_variable("PASSWORD_DB")
USER_DB = get_env_variable("USER_DB")
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = get_env_variable("AWS_S3_REGION_NAME")
AWS_UPLOAD_USER = get_env_variable("AWS_UPLOAD_USER")
AWS_UPLOAD_GROUP = get_env_variable("AWS_UPLOAD_GROUP")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_AUTH = False
EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD") 

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

#STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
