from django.urls import path
# from .views import CategoryList, CategoryDetail, ProductList, ProductDetail, OrderList, OrderDetail, OrderItemList, OrderItemDetail, UserList, UserDetail

# urlpatterns = [
#     path('categories/', CategoryList.as_view()),
#     path('categories/<int:pk>/', CategoryDetail.as_view()),
#     path('products/', ProductList.as_view()),
#     path('products/<int:pk>/', ProductDetail.as_view()),
#     path('orders/', OrderList.as_view()),
#     path('orders/<int:pk>/', OrderDetail.as_view()),
#     path('order-items/', OrderItemList.as_view()),
#     path('order-items/<int:pk>/', OrderItemDetail.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
    
# # path('checkout/user-information/', UserInformationView.as_view()),
# #     path('checkout/shipping-details/', ShippingDetailsView.as_view()),
# #     path('checkout/payment-information/', PaymentInformationView.as_view()),


# ]

from django.urls import path,include
from RomaSite.views import UserCreateView, UserDetailView

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
]

# path('', include('app_name.urls')),