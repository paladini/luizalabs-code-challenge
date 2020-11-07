from django.shortcuts import render

from rest_framework import generics
from .models import Client, Product
from .serializers import ClientSerializer, ProductSerializer

class ClientList(generics.ListCreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer