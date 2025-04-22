from .forms import BuyerAuthenticationForm
from .forms import PurchaseHistoryProductForm
from .forms import PurchaseHistoryForm
from .forms import BuyerProductForm
from .forms import BuyerCartForm
from .forms import BuyerForm
from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Buyer
from .Serializers import BuyerSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'store_name', 'phone_number']
    ordering_fields = ['created_at', 'financial_limit', 'status']
    permission_classes = [AllowAny]  # Allow all users to access for now

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({
                "message": "خریدار با موفقیت ایجاد شد.",
                "data": response.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "error": f"خطا در ایجاد خریدار: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({
                "message": "اطلاعات خریدار با موفقیت به‌روزرسانی شد.",
                "data": response.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "error": f"خطا در به‌روزرسانی اطلاعات خریدار: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response({
                "message": "خریدار با موفقیت حذف شد."
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "error": f"خطا در حذف خریدار: {str(e)}"
            }, status=status.HTTP_400_BAD_REQUEST)


# ویو برای تمپلیت ها


def buyer_form(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # پیام موفقیت یا انتقال به صفحه دیگر
                message = "اطلاعات با موفقیت ذخیره شدند."
            except Exception as e:
                # مدیریت خطا و نمایش پیام مناسب
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = BuyerForm()
        message = ""
    return render(request, 'Buyer.html', {'form': form, 'message': message})


def buyer_cart_form(request):
    if request.method == 'POST':
        form = BuyerCartForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = "اطلاعات با موفقیت ذخیره شدند."
            except Exception as e:
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = BuyerCartForm()
        message = ""
    return render(request, 'BuyerCart.html', {'form': form, 'message': message})


def buyer_product_form(request):
    if request.method == 'POST':
        form = BuyerProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = "اطلاعات محصول با موفقیت ذخیره شدند."
            except Exception as e:
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = BuyerProductForm()
        message = ""
    return render(request, 'BuyerProduct.html', {'form': form, 'message': message})


def purchase_history_form(request):
    if request.method == 'POST':
        form = PurchaseHistoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = "اطلاعات سابقه خرید با موفقیت ذخیره شدند."
            except Exception as e:
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = PurchaseHistoryForm()
        message = ""
    return render(request, 'PurchaseHistory.html', {'form': form, 'message': message})


def purchase_history_product_form(request):
    if request.method == 'POST':
        form = PurchaseHistoryProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = "اطلاعات محصول مرتبط با سابقه خرید با موفقیت ذخیره شدند."
            except Exception as e:
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = PurchaseHistoryProductForm()
        message = ""
    return render(request, 'PurchaseHistoryProduct.html', {'form': form, 'message': message})


def buyer_authentication_form(request):
    if request.method == 'POST':
        form = BuyerAuthenticationForm(
            request.POST, request.FILES)  # توجه به مدیریت فایل‌ها
        if form.is_valid():
            try:
                form.save()
                message = "اطلاعات احراز هویت با موفقیت ذخیره شدند."
            except Exception as e:
                message = f"خطایی رخ داد: {str(e)}"
        else:
            message = "لطفاً فرم را به درستی پر کنید."
    else:
        form = BuyerAuthenticationForm()
        message = ""
    return render(request, 'BuyerAuthentication.html', {'form': form, 'message': message})
