from django.db import models

class Photo(models.Model):
    uploader = models.ForeignKey(User, db_index=True, null=False, blank=False, on_delete=models.CASCADE)

    image_file = ImageField(upload_to = 'photos')
    
    added_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
