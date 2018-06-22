from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from os.path import dirname
from .settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'login/$', auth_views.login, {'template_name': BASE_DIR + '/test1/templates/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'articles/', include('test1.crud.urls')),
]
