from rest_framework import serializers
from .models import Client, Product, FavoriteList #, FavoriteList
from django.db import models


class ProductSerializer(serializers.ModelSerializer):

    # favorites = ClientSerializer(many=True, read_only=True)
    # favorited_by = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'price', 'image', 'review_score')#,'favorited_by')
        # extra_kwargs = {'favorited_by': {'required': False}}
        
class ProductFavoriteSerializer(serializers.ModelSerializer):
    
    # product = None
    # client = None
    
    class Meta:
        model = FavoriteList
        fields = ('product','client')# 'client',)
    
    # product_id = serializers.PrimaryKeyRelatedField(
        # queryset=Product.objects.all(), required=True)
    # clients = serializers.PrimaryKeyRelatedField(
        # queryset=Client.objects.all(), required=True) 
    # favorited_by = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True, required=False)
    # models.ForeignKey(ContentType)
    # id = models.ForeignKey(Product, on_delete = models.CASCADE,)
    # favoritos = ProductSerializer(many=True, read_only=True)
    # case_to_person = LitigantSerializer(many=True)
    
    # class Meta:
        # model = Product
        # fields = ('id', 'title', 'brand', 'price', 'image', 'review_score')
        
        # model = Product
        # fields = ('id',)
        
        
        

class ClientSerializer(serializers.ModelSerializer):

    favorites = ProductSerializer(many=True,read_only=True)
    # litigants = PersonSerializer(many=True, read_only=True)
    # client_to_product = ProductFavoriteSerializer(many=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'email','favorites',)#'client_to_product')
        # extra_kwargs = {'favorites': {'required': False}}
        
    # def create(self, validated_data):
    #     favorites_data = validated_data.pop('favorites')
    #     album = Client.objects.create(**validated_data)
    #     for favorite_data in favorites_data:
    #         Product.objects.create(client=favorite_data, **favorites_data)
    #     return album
        
# class FavoriteListSerializer(serializers.ModelSerializer):

#     products = serializers.PrimaryKeyRelatedField(
#         queryset=Product.objects.all(), required=True)
#     clients = serializers.PrimaryKeyRelatedField(
#         queryset=Client.objects.all(), required=True)    

#     class Meta:
#         # model = FavoriteList
#         fields = ('products', 'clients',)