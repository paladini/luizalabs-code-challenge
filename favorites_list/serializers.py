from rest_framework import serializers
from .models import Client, Product

class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = ('name', 'email')
        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ('title', 'brand', 'price', 'image', 'reviewScore')