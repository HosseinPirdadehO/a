from . import views
from django.urls import path
from django import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'buyers', views.BuyerViewSet, basename='buyer')

urlpatterns = [
    path('api/', include(router.urls)),
    path('buyer_form/', views.buyer_form, name='buyer_form'),
    path('buyer_cart_form/', views.buyer_cart_form, name='buyer_cart_form'),
    path('buyer_product_form/', views.buyer_product_form,
         name='buyer_product_form'),
    path('purchase_history_form/', views.purchase_history_form,
         name='purchase_history_form'),
    path('purchase_history_product_form/', views.purchase_history_product_form,
         name='purchase_history_product_form'),
    path('buyer_authentication_form/', views.buyer_authentication_form,
         name='buyer_authentication_form'),
]
