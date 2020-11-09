from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from django.urls import path

router = DefaultRouter()
router.register(r'clients', views.ClientList)
router.register(r'products', views.ProductList)
router.register(r'favorites', views.FavoriteListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]