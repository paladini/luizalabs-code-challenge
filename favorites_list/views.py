from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client, Product, FavoriteList
from .serializers import ClientSerializer, ProductSerializer, ProductFavoriteSerializer #, FavoriteListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

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
    serializer_class = ProductFavoriteSerializer
    
    def get_queryset(self):
        return FavoriteList.objects.all()
    
    @action(methods=['get'], detail=True)
    def add_favorite(self, request, *args, **kwargs):
        client = Client.objects.get(pk=int(kwargs['id']))
        product = Product.objects.get(pk=int(kwargs['product_id']))
        
        favoriteList, created = FavoriteList.objects.get_or_create(product=product, client=client)
        serializer = ClientSerializer(client, many=False)
        return JsonResponse(serializer.data, safe=False)
    
    @action(methods=['get, delete'], detail=True)
    def remove_favorite(self, request, *args, **kwargs):
        client = Client.objects.get(pk=int(kwargs['id']))
        product = Product.objects.get(pk=int(kwargs['product_id']))
        
        try:
            favoriteList = FavoriteList.objects.get(product=product, client=client)
            favoriteList.delete()
        except FavoriteList.DoesNotExist:
            pass    
        
        serializer = ClientSerializer(client, many=False)
        return JsonResponse(serializer.data, safe=False)