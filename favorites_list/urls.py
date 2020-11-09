from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

client_list = views.ClientList.as_view({
    'get': 'list', 
    'post': 'create'
})
client_detail = views.ClientList.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})
product_list = views.ProductList.as_view({
    'get': 'list', 
    'post': 'create'
})
product_detail = views.ProductList.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})
favorites_list = views.FavoriteListViewSet.as_view({
    'get': 'list', 
    'post': 'create'
})
favorite_detail = views.FavoriteListViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})


urlpatterns = [
    url(r'^clients/$', client_list, name='client-list'),
    url(r'^clients/<int:id>/', client_detail, name='client-detail'),
    url(r'^products/$', product_list, name='product-list'),
    url(r'^products/<int:id>/', product_detail, name='product-detail'),
    url(r'^favorites/$', favorites_list, name='favorite-list'),
    url(r'^favorites/<int:id>/', favorite_detail, name='favorite-detail'),
]