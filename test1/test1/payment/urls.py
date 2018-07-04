from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'create', views.pay, name='pay'),
    url(r'cancel', views.pay_cancel, name='pay_cancel'),\
    url(r'success', views.pay_success, name='pay_success'),
    #url(r'success\?paymentId=PAY-(?P<paymentId>[0-9A-Z]+)&token=EC-(?P<token>[0-9A-Z]+)&PayerID=(?P<PayerID>[0-9A-Z]+)', views.pay_success, name='pay_success'),
]
