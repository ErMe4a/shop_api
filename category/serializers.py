from rest_framework import serializers

from product.serializer import ProductListSerializer
from .models import Category 



class CategoryListSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields= '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products']=ProductListSerializer(instance.products.all(), many=True).data
        return representation

    

# class CategoryDetailSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
