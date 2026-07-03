from django.conf import settings
from storages.backends.s3 import S3Storage


class SupabaseStorage(S3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        return settings.MEDIA_URL + name