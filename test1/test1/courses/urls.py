from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'view/', views.courses_view, name='courses'),
    url(r'task/$', views.create_task, name='create_task'),
    url(r'task/(?P<task_status_id>.*)/$', views.task_view, name='task_view'),
    url(r'task/(?P<task_status_id>.*)/send$', views.send_task, name='send_task'),
    url(r'task/(?P<task_status_id>.*)/sendback', views.send_task_back, name='send_task_back'),
    url(r'task/(?P<task_status_id>.*)/accept', views.accept_task, name='accept_task'),
]
