# Generated by Django 2.0.6 on 2018-06-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180627_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='imagekit'),
        ),
    ]