from django.urls import path
from Checkout.views import OrderDetail,OrderListView
from Checkout.views import ShippingAddressListCreateView,PaymentListCreateView,UserInformationView
from Checkout.views import checkout,register_user,CustomAuthToken

from django.urls import path


urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),

    path('shipping-addresses/', ShippingAddressListCreateView.as_view(), name='shipping-addresses'),
    path('payments/', PaymentListCreateView.as_view(), name='payments'),
    path('user-information/', UserInformationView.as_view()),
    path('api/checkout/', checkout, name='checkout'),
    path('token/', CustomAuthToken.as_view(), name='token'),
    path('register/', register_user, name='register-user'),


]
# from django.urls import path
# from .views import (
#     checkout,
#     OrderDetail,
#     OrderListView,
#     ShippingAddressListCreateView,
#     PaymentListCreateView,
#     UserInformationView,
#     CustomAuthToken,
#     register_user
# )

# urlpatterns = [
#     path('api/checkout/', checkout, name='checkout'),
#     path('api/order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
#     path('api/orders/', OrderListView.as_view(), name='order-list'),
#     path('api/shipping-address/', ShippingAddressListCreateView.as_view(), name='shipping-address'),
#     path('api/payment/', PaymentListCreateView.as_view(), name='payment'),
#     path('api/user-information/', UserInformationView.as_view(), name='user-information'),
#     path('api/token/', CustomAuthToken.as_view(), name='token'),
#     path('api/register/', register_user, name='register-user'),
# ]