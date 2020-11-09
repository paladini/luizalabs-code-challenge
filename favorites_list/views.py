from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client, Product, FavoriteList
from .serializers import ClientSerializer, ProductSerializer, FavoriteListSerializer
from rest_framework.permissions import IsAuthenticated

class ClientList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ProductList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class FavoriteListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer