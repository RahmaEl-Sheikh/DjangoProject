# # import genericpath
# # from types import GenericAlias
# # from django.shortcuts import render
# # from Checkout.models import OrderItem

# # from rest_framework.generics import ListAPIView, RetrieveAPIView
# # from Checkout.serializers import OrderItemSerializer, OrderSerializer

# # from rest_framework import status
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response

# # # Create your views here.
# # class OrderListView(genericpath.ListAPIView):
# #     serializer_class = OrderSerializer

# #     def get_queryset(self):
# #         return OrderItem.objects.filter(user=self.request.user)

# # class OrderDetailView(GenericAlias.RetrieveAPIView):
# #     queryset = OrderItemSerializer.objects.all()
# #     serializer_class = OrderSerializer
# from django.urls import path
# from Checkout.views import OrderListView, OrderDetailView

# # urlpatterns = [
# #     path('orders/', OrderListView.as_view(), name='order-list'),
# #     path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
# # ]

# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.shortcuts import render
# from Checkout.models import OrderItem

# from Checkout.serializers import OrderItemSerializer, OrderSerializer

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.
# class OrderListView(ListAPIView):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         return OrderItem.objects.filter(user=self.request.user)

# class OrderDetailView(RetrieveAPIView):
#     queryset = OrderItemSerializer.objects.all()
#     serializer_class = OrderSerializer

   

# @api_view(['POST'])
# def checkout(request):
#     serializer = OrderSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save(user=request.user)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)

# from rest_framework.generics import ListAPIView
# , RetrieveAPIView
# from django.shortcuts import render
# from Checkout.models import OrderItem

# from Checkout.serializers import OrderItemSerializer, OrderSerializer

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.
# class OrderListView(ListAPIView):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         return OrderItem.objects.filter(user=self.request.user)

# class OrderDetailView(RetrieveAPIView):
#     queryset = OrderItemSerializer.objects.all()
#     serializer_class = OrderSerializer


# from django.shortcuts import render
# from Checkout.models import Order, OrderItem

# from Checkout.serializers import OrderItemSerializer, OrderSerializer

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.

# class OrderDetailView(RetrieveAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from .models import Order
from .serializers import OrderSerializer
from rest_framework import serializers
from Checkout.models import OrderItem,Order

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
fields = ['id', 'user', 'date_created', 'date_updated', 'status', 'total', 'items']

from rest_framework.generics import ListAPIView, RetrieveAPIView

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):

    # your checkout logic here
    return Response(status=201)


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderListView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

from rest_framework import generics, permissions
from .models import ShippingAddress, Payment,UserInformation
from .serializers import ShippingAddressSerializer, PaymentSerializer,UserInformationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import AllowAny



class ShippingAddressListCreateView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
     serializer.save(user=self.request.user)

class UserInformationView(generics.CreateAPIView):
    serializer_class = UserInformationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = UserInformation.objects.create(
            user=request.user,
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            phone_number=serializer.validated_data['phone_number']
        )
        return Response(serializer.data)
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id
        })


@api_view(['POST'])
@permission_classes(([[AllowAny]]))
def register_user(request):
    # your registration logic here
    return Response(status=201)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def my_public_view(request):
#     # Your view logic here
#     return Response({'message': 'This is a public view'})

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token,authenticate
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['POST'])
# def generate_token(request):
#     """
#     Generate a token for a user
#     """
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     # Authenticate the user
#     user = authenticate(username=username, password=password)

#     # If the user is authenticated, generate a token
#     if user is not None:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#     else:
#         return Response({'error': 'Invalid credentials'})
