from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from django.urls import path
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r'clients', views.ClientList)
router.register(r'products', views.ProductList)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:id>/favorites/<int:product_id>/', views.FavoriteListViewSet.as_view({"get": "add_favorite"})),
    path('clients/<int:id>/favorites/<int:product_id>/remove', views.FavoriteListViewSet.as_view({"get": "remove_favorite"}))
]