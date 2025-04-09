from .forms import RequestActivationForm, FinanciallySettledForm, PaymentForm, BuyerPaymentForm, FinanciallySettledForm, ProductPaymentForm, MarketerPaymentForm
from .models import RequestActivation, FinanciallySettled, Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment, BuyerPayment, FinanciallySettled
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters, status, permissions
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.response import Response
from .Serializers import PaymentSerializer, MarketerPaymentSerializer, HistoryMarketerPaymentSerializer, ProductPaymentSerializer, BuyerPaymentSerializer, FinanciallySettledSerializer, RequestActivationSerializer
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

# مالی خریدار تسویه کننده

# api FinanciallySettledViewSet->


class FinanciallySettledViewSet(viewsets.ModelViewSet):
    queryset = FinanciallySettled.objects.all()
    serializer_class = FinanciallySettledSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number', 'product_name']
    permission_classes = [permissions.AllowAny]  # دسترسی آزاد برای کاربران

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({"message": "اطلاعات مالی با موفقیت به‌روزرسانی شد.", "data": response.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"خطا در به‌روزرسانی اطلاعات مالی: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            response = super().destroy(request, *args, **kwargs)
            return Response({"message": "اطلاعات مالی با موفقیت حذف شد."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"خطا در حذف اطلاعات مالی: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


# فرم اصلی مالی خریدار تسویه شده


def financially_settled_form(request):
    try:
        if request.method == 'POST':
            form = FinanciallySettledForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'success.html', {"message": "فرم با موفقیت ثبت شد."})
            else:
                return render(request, 'FinanciallySettled.html', {'form': form, 'error': 'لطفاً تمام فیلدها را به درستی پر کنید.'})
        else:
            form = FinanciallySettledForm()
        return render(request, 'FinanciallySettled.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در پردازش فرم: {str(e)}"})

# دیتیل فرم


def financially_settled_detail(request, pk):
    try:
        settlement = get_object_or_404(FinanciallySettled, pk=pk)
        return render(request, 'FinanciallySettledDetail.html', {'settlement': settlement})
    except FinanciallySettled.DoesNotExist:
        return HttpResponse("اطلاعات تسویه‌حساب یافت نشد.", status=404)
    except Exception as e:
        return HttpResponse(f"خطای غیرمنتظره رخ داده است: {str(e)}", status=500)

# لیست تسویه شده ها


def financially_settled_list(request):
    try:
        settlements = FinanciallySettled.objects.all()
        return render(request, 'FinanciallySettledList.html', {'settlements': settlements})
    except Exception as e:
        return render(request, 'error.html', {'message': f"خطا در بارگذاری لیست تسویه‌حساب‌ها: {str(e)}"})

# درخواست تسویه زمان دار


class RequestActivationViewSet(viewsets.ModelViewSet):
    queryset = RequestActivation.objects.all()
    serializer_class = RequestActivationSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی آزاد

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# view template


def request_activation_form_view(request):
    if request.method == 'POST':
        form = RequestActivationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
    else:
        form = RequestActivationForm()
    return render(request, 'RequestActivation.html', {'form': form})
