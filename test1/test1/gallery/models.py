import os
from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField, StdImageFieldFile
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from .helpers import UploadToIdNameDir

class ImageFieldFile(StdImageFieldFile):
    @classmethod
    def get_variation_name(cls, file_name, variation_name):
        """Return the variation file name based on the variation."""
        path, ext = os.path.splitext(file_name)
        path, file_name = os.path.split(path)
        file_name = '{file_name}.{extension}'.format(**{
            'file_name': file_name,
            'extension': ext,
        })
        return os.path.join(path, variation_name, file_name)

class ImageField(StdImageField):
    attr_class = ImageFieldFile

class Photo(models.Model):
    uploader = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)

    image_file = ImageField(upload_to=UploadToIdNameDir('photo'), blank=True, variations={
        '1': (600, 400),
        '2': (300, 200),
        '3': (100, 100, True),
    })


    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
