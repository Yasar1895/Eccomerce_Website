from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, OrderList

urlpatterns = [
    path('products/', ProductList.as_view(), name='api_products'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='api_product_detail'),
    path('categories/', CategoryList.as_view(), name='api_categories'),
    path('orders/', OrderList.as_view(), name='api_orders'),
]
