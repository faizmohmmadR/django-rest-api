from rest_framework import generics
from .models import Product
from .serializers import ProductSerialize
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerialize
    queryset = Product.objects.all()

class ProductDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerialize
    queryset = Product.objects.all()