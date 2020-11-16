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
    
    # @action(detail=False, methods=['post'])
    # def add_favorite(self, request, pk=None):
        
    
        
        # client_obj = Client.objects.get(pk=pk).
        
        # page = self.paginate_queryset(recent_users)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(recent_users, many=True)
        # return Response(serializer.data)
        
        
        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)
    
    
class ProductList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class FavoriteListViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)  
    serializer_class = ProductFavoriteSerializer
    
    def get_queryset(self):
        return FavoriteList.objects.all() #filter(favorited_by=self.kwargs['product_id'])
    
    @action(methods=['get'], detail=False)
    def add_favorite(self, request, *args, **kwargs):
        # client = self.get_object()
        # client = int(kwargs['client_pk'])
        client = Client.objects.get(pk=int(kwargs['id']))
        product = Product.objects.get(pk=int(kwargs['product_id']))
        # FavoriteList.objects.create(product=product, client=client)
        print("\n\nLOG:\n")
        print(client)
        print(product)
        print("\n\n\n")
        
        favoriteList, created = FavoriteList.objects.get_or_create(product=product, client=client)
        serializer = ProductFavoriteSerializer(favoriteList, many=False)
        return JsonResponse(serializer.data, safe=False)
        # return Response(favoriteList)
        # return Response(status=status.HTTP_204_NO_CONTENT)
    
# class FavoriteListViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)  
    # serializer_class = ProductFavoriteSerializer
    
    # @action(detail=True, methods=['post'])
    # def add_favorite(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    
    # def add(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def remove(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
        # return Response(serializer.data)
    
    # def get_queryset(self):
        # return Product.objects.filter(favorited_by=self.kwargs['client_pk'])