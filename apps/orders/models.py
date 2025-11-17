from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('paid','Paid'),
        ('shipped','Shipped'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'Order {self.id} - {self.status}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product_name} x {self.quantity}'
