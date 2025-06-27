from django.urls import path
from .views import product_list, product_detail, order_list, order_detail, recommend_products

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('orders/', order_list, name='order-list'),
    path('orders/<int:pk>/', order_detail, name='order-detail'),
    path('recommend/', recommend_products, name='recommend-products'),
] 