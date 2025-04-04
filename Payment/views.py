from .forms import BuyerPaymentForm
from .forms import ProductPaymentForm
from .forms import MarketerPaymentForm
from django.shortcuts import render, redirect
from .forms import PaymentForm
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment, BuyerPayment
from .Serializers import PaymentSerializer, MarketerPaymentSerializer, HistoryMarketerPaymentSerializer, ProductPaymentSerializer, BuyerPaymentSerializer
from rest_framework import status, permissions
# Create your views here.


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'store_name']
    ordering_fields = ['debt', 'financial_limit']
    # دسترسی برای خواندن عمومی و ویرایش برای احراز هویت‌شده‌ها
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی ازاد

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({"message": "پرداخت جدید با موفقیت ایجاد شد!", "data": response.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"خطا در ایجاد پرداخت: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class MarketerPaymentViewSet(viewsets.ModelViewSet):
    queryset = MarketerPayment.objects.all()
    serializer_class = MarketerPaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'role']
    ordering_fields = ['wallet_balance', 'status']
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی ازاد

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "پرداخت بازاریاب حذف شد."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": f"خطا در حذف پرداخت بازاریاب: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class HistoryMarketerPaymentViewSet(viewsets.ModelViewSet):
    queryset = HistoryMarketerPayment.objects.all()
    serializer_class = HistoryMarketerPaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['history', 'payment_date']
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی ازاد

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({"message": "سابقه بازاریاب با موفقیت به‌روزرسانی شد.", "data": response.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"خطا در به‌روزرسانی سابقه: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class ProductPaymentViewSet(viewsets.ModelViewSet):
    queryset = ProductPayment.objects.all()
    serializer_class = ProductPaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['product_name']
    ordering_fields = ['purchase_price', 'sale_price', 'stock']
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی ازاد


class BuyerPaymentViewSet(viewsets.ModelViewSet):
    queryset = BuyerPayment.objects.all()
    serializer_class = BuyerPaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'store_name']
    ordering_fields = ['debt', 'financial_limit']
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی ازاد

# ویو برای تمپلیت ها

# مالی اصلی


def create_payment(request):
    try:
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # ریدایرکت به صفحه موفقیت
        else:
            form = PaymentForm()
        return render(request, 'Main_payment.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در ایجاد پرداخت: {str(e)}"})

# مالی بازاریاب


def create_marketer_payment(request):
    try:
        if request.method == 'POST':
            form = MarketerPaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')
        else:
            form = MarketerPaymentForm()
        return render(request, 'MarketerPayment.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در ایجاد پرداخت بازاریاب: {str(e)}"})

# مالی محصول


def create_product_payment(request):
    try:
        if request.method == 'POST':
            form = ProductPaymentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success_page')
        else:
            form = ProductPaymentForm()
        return render(request, 'ProductPayment.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در ایجاد مالی محصول: {str(e)}"})

# مالی خریدار


def create_buyer_payment(request):
    try:
        if request.method == 'POST':
            form = BuyerPaymentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')
        else:
            form = BuyerPaymentForm()
        return render(request, 'BuyerPayment.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در ایجاد مالی خریدار: {str(e)}"})


def success_page(request):
    return render(request, 'success_page.html', {'message': 'عملیات با موفقیت انجام شد!'})


def error_page(request):
    return render(request, 'error.html', {'message': 'مشکلی پیش آمده است!'})
