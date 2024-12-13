from django.db import models
from products.models import Product 
from django.contrib.auth import get_user_model 

User = get_user_model() 
# Create your models here.
ORDER_STATUSES = (
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Delivered', 'Delivered'),
)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default='Pending')