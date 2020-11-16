from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from django.urls import path
from rest_framework_nested import routers

router = DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'clients', views.ClientList)
router.register(r'products', views.ProductList)
# router.register(r'favorites', views.FavoriteListViewSet)

# domains_router = routers.NestedSimpleRouter(router, r'clients', lookup='client')
# domains_router.register(r'favorites', views.FavoriteListViewSet, basename='client-favorites')

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^', include(domains_router.urls)),
    path('clients/<int:id>/favorites/<int:product_id>/', views.FavoriteListViewSet.as_view({"get": "add_favorite"}))
]