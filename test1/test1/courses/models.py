from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Course(MPTTModel):
    name = models.CharField(max_length=50, unique=True, db_index=True, null=False, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
