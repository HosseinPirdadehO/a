from django.urls import path
from .views import order_view, success_view, error_view

urlpatterns = [
    path('order/', order_view, name='order'),  # URL برای فرم سفارش
    path('success/', success_view, name='success'),  # URL برای صفحه موفقیت
    path('error/', error_view, name='error'),  # URL برای صفحه خطا
]
