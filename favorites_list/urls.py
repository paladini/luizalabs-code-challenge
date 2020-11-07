from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clients/$', views.ClientList.as_view(), name='client-list'),
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
]