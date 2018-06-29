from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from .authentification import views
from .settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from .views import react_test

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>.*)/(?P<token>.*)/$',
        views.activate, name='activate'),
    url(r'login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'articles/', include('test1.crud.urls')),
    url(r'gallery/', include('test1.gallery.urls')),
    url(r'pay/', include('test1.payment.urls')),
    url(r'courses/', include('test1.courses.urls')),
    path('react/', react_test, name='react_test'),
    #url(r'social/', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
