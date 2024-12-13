from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, OrderSerializer
from products.models import Product, Category 
from django.contrib.auth import get_user_model
from orders.models import Order 
from rest_framework.permissions import IsAuthenticated  

User = get_user_model()

# Create your views here.
class UserViewSet(ReadOnlyModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] 

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    