from . import views
from django.urls import path
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet,
                basename='product-image')

urlpatterns = [
    path('api/', include(router.urls)),

    path('product/create/', views.create_product, name='create_product'),
    path('success/', views.success_page, name='success_page'),
    path('error/', views.error_page, name='error_page'),
]

# آدرس
# "products": "http://127.0.0.1:8000/Product/api/products/"
