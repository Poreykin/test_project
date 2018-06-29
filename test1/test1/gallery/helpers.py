import os
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToIdNameDir(object):
    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        user = instance.uploader
        id_dir = str(instance.uploader.pk)
        return os.path.join(self.sub_path, id_dir, filename)
