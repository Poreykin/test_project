from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .authentification import views
from .settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>.*)/(?P<token>.*)/$',
        views.activate, name='activate'),
    url(r'login/$', auth_views.login, {'template_name': BASE_DIR + '/test1/templates/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'articles/', include('test1.crud.urls')),
]
