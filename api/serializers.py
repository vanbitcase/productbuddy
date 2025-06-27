from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, write_only=True, source='products')

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'products', 'product_ids'] 