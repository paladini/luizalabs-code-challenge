from django.shortcuts import render

from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer

class ClientList(generics.ListCreateAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer