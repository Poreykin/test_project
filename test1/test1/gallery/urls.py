from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'view/$', views.gallery_view, name='gallery_view'),
    url(r'view/(?P<photo_id>.*)', views.gallery_view, name='gallery_view'),
    url(r'upload', views.upload_photo, name='upload_photo'),
    #url(r'delete/(?P<photo_id>.*)', views.delete_photo, name='delete_photo'),
]
