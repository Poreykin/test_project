from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'view/$', views.articles_view, name='articles_view'),
    url(r'view/(?P<article_name>.*)', views.articles_view, name='articles_view'),
    url(r'create', views.create_article, name='create_article'),
    url(r'update/(?P<article_name>.*)', views.update_article, name='update_article'),
    url(r'delete/(?P<article_name>.*)', views.delete_article, name='delete_article'),
]
