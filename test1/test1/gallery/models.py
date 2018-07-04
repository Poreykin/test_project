import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from stdimage.models import StdImageField, StdImageFieldFile
from .helpers import UploadToClassNameDir

class ImageFieldFile(StdImageFieldFile):
    @classmethod
    def get_variation_name(cls, file_name, variation_name):
        """Return the variation file name based on the variation."""
        path, ext = os.path.splitext(file_name)
        path, file_name = os.path.split(path)
        file_name = '{variation_name}_{file_name}{extension}'.format(**{
            'variation_name': variation_name,
            'file_name': file_name,
            'extension': ext,
        })
        return os.path.join(path, file_name)

class ImageField(StdImageField):
    attr_class = ImageFieldFile

class UploadFilesToIdDirModel(models.Model):
    UPLOAD_FILES = {}
    
    class Meta:
        abstract = True

    def get_final_name(self, final_dest, file_name):
        name, ext = os.path.splitext(file_name)
        path, name = os.path.split(name)
        final_name = os.path.join(str(self.pk), '%s%s' % (name, ext,))
        if callable(final_dest):
            return final_dest(self, final_name)
        else:
            return os.path.join(final_dest, final_name)

    def save(self, force_insert=False, force_update=False):
        upload_files = getattr(self, 'UPLOAD_FILES', None)
        if upload_files:
            super(UploadFilesToIdDirModel, self).save(force_insert, force_update)
            force_insert, force_update = False, True
            
            for base_field_name, options in upload_files.items():
                base_field = getattr(self, base_field_name)
                fields = {base_field_name: base_field}
                final_dest = options['dest']
                file_name = force_str(base_field)
                base_final_name = self.get_final_name(final_dest, file_name)
                if file_name != base_final_name:
                    base_field.storage.delete(base_final_name)
                    base_field.storage.save(base_final_name, base_field)
                    base_field.storage.delete(force_str(base_field))
                    setattr(self, base_field_name, base_final_name)
                variations = options.get('variations', set())
                final_name = dict()
                for field_name in variations:
                    field = getattr(base_field, field_name)
                    file_name = force_str(field)
                    final_name[field_name] = self.get_final_name(final_dest, file_name)
                    if file_name != final_name[field_name]:
                        field.storage.delete(final_name[field_name])
                        field.storage.save(final_name[field_name], field)
                        field.storage.delete(force_str(field))
                        setattr(base_field, field_name, final_name[field_name])
        
        super(UploadFilesToIdDirModel, self).save(force_insert, force_update)

class Photo(UploadFilesToIdDirModel):
    uploader = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)

    image_file = ImageField(upload_to=UploadToClassNameDir('public/uploads', 'image_file/tmp'), blank=True, variations={
        'large': (600, 400),
        'medium': (300, 200),
        'small': (100, 100, True),
    })
    UPLOAD_FILES = {'image_file': {'dest': UploadToClassNameDir('public/uploads', 'image_file'), 'variations': {'large', 'medium', 'small'}}}

    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
