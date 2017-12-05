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
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = get_env_variable("AWS_S3_REGION_NAME")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

#STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"
STATICFILES_STORAGE = 'storage.backends.s3boto3.S3Boto3Storage'
