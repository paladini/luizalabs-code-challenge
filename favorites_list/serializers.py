from rest_framework import serializers
from .models import Client, Product, FavoriteList
from django.db import models


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'price', 'image', 'review_score')
        
class ProductFavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavoriteList
        fields = ('product','client')
        

class ClientSerializer(serializers.ModelSerializer):

    favorites = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'email','favorites',)