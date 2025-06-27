from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    domain = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders')
   

    def __str__(self):
        return f"Order {self.id} at {self.created_at}"
