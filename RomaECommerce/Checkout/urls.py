from django.urls import path
from Checkout.views import OrderDetail,OrderListView
from Checkout.views import ShippingAddressListCreateView,PaymentListCreateView
urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
urlpatterns = [
    path('shipping-addresses/', ShippingAddressListCreateView.as_view(), name='shipping-addresses'),
    path('payments/', PaymentListCreateView.as_view(), name='payments'),
]
