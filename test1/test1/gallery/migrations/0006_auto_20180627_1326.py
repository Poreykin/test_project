# Generated by Django 2.0.6 on 2018-06-27 08:26

from django.db import migrations
import test1.gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20180627_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_thumbnail',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=test1.gallery.models.ImageField(blank=True, upload_to='stdimage'),
        ),
    ]
