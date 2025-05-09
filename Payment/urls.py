from .views import RequestActivationViewSet
from django.urls import path
from .views import FinanciallySettledViewSet, PaymentViewSet, MarketerPaymentViewSet, HistoryMarketerPaymentViewSet, ProductPaymentViewSet, BuyerPaymentViewSet, request_activation_form_view
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'marketer-payments', MarketerPaymentViewSet)
router.register(r'history-marketer-payments', HistoryMarketerPaymentViewSet)
router.register(r'product-payments', ProductPaymentViewSet)
router.register(r'buyer-payments', BuyerPaymentViewSet)
router.register(r'financially-settled', FinanciallySettledViewSet,
                basename='financially-settled')
router.register(r'RequestActivation', RequestActivationViewSet,
                basename='requestactivation')


urlpatterns = [
    path('api/', include(router.urls)),

    path('payment/create/', views.create_payment,
         name='create_payment'),  # (مالی اصلی)
    path('marketer-payment/create/', views.create_marketer_payment,  # (مالی بازاریاب)
         name='create_marketer_payment'),
    path('product-payment/create/', views.create_product_payment,  # (مالی محصول)
         name='create_product_payment'),
    path('buyer-payment/create/', views.create_buyer_payment,  # (مالی خریدار)
         name='create_buyer_payment'),
    path('success/', views.success_page, name='success_page'),
    path('error/', views.error_page, name='error_page'),
    ##
    path('api/', include(router.urls)),  # مالی خریدار تسویه شده

    path('financially-settled/', views.financially_settled_list,
         name='financially_settled_list'),
    path('financially-settled-form/', views.financially_settled_form,
         name='financially_settled_form'),
    path('financially-settled/<int:pk>/', views.financially_settled_detail,
         name='financially_settled_detail'),

    path('api/', include(router.urls)),  # درخواست تسویه زمان دار
    path('request_activation_view/',
         request_activation_form_view, name='RequestActivation'),
]


# آدرس ای پی ای ها
# {"payments":"http://127.0.0.1:8000/Payment/api/payments/","marketer-payments":"http://127.0.0.1:8000/Payment/api/marketer-payments/","history-marketer-payments":"http://127.0.0.1:8000/Payment/api/history-marketer-payments/","product-payments":"http://127.0.0.1:8000/Payment/api/product-payments/","buyer-payments":"http://127.0.0.1:8000/Payment/api/buyer-payments/"}
