import os
import uuid
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToClassNameDir(object):
    def __init__(self, path, sub_dir):
        self.sub_path = path
        self.sub_dir = sub_dir

    def __call__(self, instance, filename):
        class_name = instance.__class__.__name__.lower()
        return os.path.join(self.sub_path, class_name, self.sub_dir, filename)
