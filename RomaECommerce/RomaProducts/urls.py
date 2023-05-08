# from django.urls import path
# from .views import CategoryListView, CategoryDetailView
# from .serializers import CategorySerializer

# app_name = 'RomaProducts'

# urlpatterns = [
#     path('categories/', CategoryListView.as_view()),
#     path('categories/<int:pk>/', CategoryDetailView.as_view()),
# ]

from django.urls import path,include
# from RomaProducts.views import CategoryListView, CategoryCreateView, CategoryDetailView, ProductCreateView, ProductDetailView
from RomaProducts.views import CategoryCreateView, ProductCreateView, ProductList,ProductDetail,CategoryList,CategoryDetail
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:pk>/products/', ProductList.as_view(), name='category-product-list'),
    path('Products/create/', ProductCreateView.as_view(), name='Product-create'),
    path('Products/<int:pk>/', ProductDetail.as_view(), name='Product-detail'),
]
# path('app_name/', include('app_name.urls')),