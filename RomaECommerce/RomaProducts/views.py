from django.shortcuts import render

# Create your views here.
# from rest_framework import viewsets
# from .models import Category, Product
# from .serializers import CategorySerializer, ProductSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

from rest_framework import generics
# from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     class ProductListView(generics.ListAPIView):
#       queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filterset_fields = ['category', 'name']

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework import authentication, permissions


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
# ,OrderSerializer,Order
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class OrderHistory(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)   
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id
        })


@api_view(['POST'])
@permission_classes(())
def register_user(request):
    # your registration logic here
    return Response(status=201)
