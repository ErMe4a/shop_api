from urllib import response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from .models import Product
from . import serializer
from rest_framework.decorators import action
from rating.serializer import ReviewSerializer
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializer.ProductListSerializer
        return serializer.ProductDetailSerializer
    
    #api/v1/products/<id>/rewiews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method =='GET':
            reviews =  product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data
            return response.Response(serializer, status = 200)
        data = request.data 
        serializer = ReviewSerializer(data = data, context={'request':request, 'product':product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)






    

