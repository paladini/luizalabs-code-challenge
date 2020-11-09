from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from django.urls import path

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


# urlpatterns = [
#     url(r'^clients/$', client_list, name='client-list'),
#     url(r'^clients/<int:pk>/', client_detail, name='client-detail'),
#     url(r'^products/$', product_list, name='product-list'),
#     url(r'^products/<int:pk>/', product_detail, name='product-detail'),
#     url(r'^favorites/$', favorites_list, name='favorite-list'),
#     url(r'^favorites/<int:pk>/', favorite_detail, name='favorite-detail'),
# ]

router = DefaultRouter()
router.register(r'clients', views.ClientList)
router.register(r'products', views.ProductList)
router.register(r'favorites', views.FavoriteListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]