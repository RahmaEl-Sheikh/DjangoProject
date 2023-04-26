# from django.db import models
# # from RomaProducts.serializers import Category,Product
# # from django.urls import path
# from RomaProducts.models import Category, Product
# from RomaProducts.serializers import CategorySerializer, ProductSerializer

# # from rest_framework import serializers


# # # Create your models here.


# # class Category(models.Model):
# #     name = models.CharField(max_length=255)

# # class Product(models.Model):
# #     name = models.CharField(max_length=255)
# #     description = models.TextField()
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     price = models.DecimalField(max_digits=6, decimal_places=2)

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name
    
#     class Product(models.Model):
#       name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Order(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField(default=1)
#     buying_date = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.product.title