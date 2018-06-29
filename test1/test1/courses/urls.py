from django.conf.urls import url
from django.urls import path
from .views import courses_view

urlpatterns = [
    url(r'view/', courses_view, name='courses'),
]
