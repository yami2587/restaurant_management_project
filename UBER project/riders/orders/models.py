# File: orders/models.py
from django.db import models
from django.contrib.auth.models import User
from .order_status import OrderStatus  # ✅ make sure this is imported if in a separate file
# or: from .models import OrderStatus (if in the same file)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # ✅ NEW: Link order to its status
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
