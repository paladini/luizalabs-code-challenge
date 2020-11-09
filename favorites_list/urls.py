from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'clients', views.ClientList.as_view, basename='client')
# router.register(r'products', views.ProductList.as_view, basename='product')
# router.register(r'favorites', views.FavoriteListViewSet, basename='favorite')
# urlpatterns = router.urls

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

urlpatterns = [
    url(r'^clients/$', client_list, name='client-list'),
    url(r'^clients/<int:id>/', client_detail, name='client-detail'),
    url(r'^products/$', product_list, name='product-list'),
    url(r'^products/<int:id>/', product_detail, name='product-detail'),
    url(r'^favorites/$', views.FavoriteListViewSet.as_view(), name='favorite-list'),
]