from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from test1.courses.models import Course

admin.site.register(Course, MPTTModelAdmin)
