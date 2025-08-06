from django.db import models
from django.contrib.auth.models import User
from restaurant.models import Menu

class Order(models.Model):
    STATUS_CHOICE = [
        ('pending','pending'),('confirmed','confirmed'),('delivered','delivered'),('cancelled','cancelled'),
    ]
    customer = models.ForeignKey(User,on_delete = models.CASCADE)
    order_items = models.ManyToManyField(Menu)
    total_amount = models.DecimalField(max_digits=8,decimal_places = 2)
    status = models.CharField(max_length=20,choices = STATUS_CHOICE,default = 'pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} by {self.customer.username}'

