from django.urls import path 
from .views import ProductList , ProductDetail

urlpatterns = [
 path("product/",ProductList.as_view()),
 path("product/<int:pk>/",ProductDetail.as_view())
]