from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client, Product, FavoriteList
from .serializers import ClientSerializer, ProductSerializer, FavoriteListSerializer


class ClientList(viewsets.ModelViewSet):

    # queryset = Client.objects.all()
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    # def retrieve(self, request, pk=None):
    #     queryset = Client.objects.all()
    #     client = get_object_or_404(queryset, pk=pk)
    #     serializer = ClientSerializer(client)
    #     return Response(serializer.data)
    
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class FavoriteListViewSet(generics.ListCreateAPIView):

    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer