from rest_framework import serializers
from .models import Client, Product, FavoriteList

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('title', 'brand', 'price', 'image', 'review_score', 'favorited',)

class ClientSerializer(serializers.ModelSerializer):

    favorites = ProductSerializer(many=True) 

    class Meta:

        model = Client
        fields = ('name', 'email',)
        

        
# class FavoriteListSerializer(serializers.HyperlinkedModelSerializer):
class FavoriteListSerializer(serializers.ModelSerializer):

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all())

    class Meta:
        model = FavoriteList
        fields = ('product', 'client', )