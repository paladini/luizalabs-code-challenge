from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from .models import Client, Product, FavoriteList
from .serializers import ClientSerializer, ProductSerializer, FavoriteListSerializer

class ClientList(generics.ListCreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class FavoriteListViewSet(generics.ListCreateAPIView):

    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer