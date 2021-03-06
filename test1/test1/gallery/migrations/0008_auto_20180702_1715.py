# Generated by Django 2.0.6 on 2018-07-02 12:15

from django.db import migrations
import test1.gallery.helpers
import test1.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20180627_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_thumbnail',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image_thumbnail2',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image_thumbnail3',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=test1.gallery.models.ImageField(blank=True, upload_to=test1.gallery.helpers.UploadToClassNameDir('public/uploads', 'image_file/tmp')),
        ),
    ]
