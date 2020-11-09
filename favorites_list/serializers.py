from rest_framework import serializers
from .models import Client, Product, FavoriteList

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('id', 'title', 'brand', 'price', 'image', 'review_score',)

class ClientSerializer(serializers.ModelSerializer):

    favorites = ProductSerializer(many=True)

    class Meta:

        model = Client
        fields = ('id', 'name', 'email','favorites',)
        
class FavoriteListSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    clients = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all())

    class Meta:
        model = FavoriteList
        fields = ('id', 'products', 'clients',)