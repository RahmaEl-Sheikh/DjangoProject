# from rest_framework import serializers
# from RomaProducts.models import Category, Product

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'description']

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price', 'category']
from .models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']