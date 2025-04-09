
from rest_framework import viewsets
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ProductForm
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, ProductImage
from .Serializers import ProductSerializer, ProductImageSerializer
from rest_framework import status, permissions

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category', 'brand']
    ordering_fields = ['purchase_price', 'sale_price',
                       'stock', 'expiration_date']
    ordering = ['-created_at']
    # محدود کردن دسترسی به کاربران احراز هویت‌شده
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]  # اجازه دسترسی آزاد

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response(
                {"message": "محصول جدید با موفقیت ایجاد شد!", "data": response.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": f"خطا در ایجاد محصول: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {"message": "محصول با موفقیت به‌روزرسانی شد.", "data": response.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": f"خطا در به‌روزرسانی محصول: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {"message": "محصول با موفقیت حذف شد."},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": f"خطا در حذف محصول: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

# ویو برای تمپلیت ها


def create_product(request):
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # ریدایرکت به صفحه موفقیت
        else:
            form = ProductForm()
        return render(request, 'Product.html', {'form': form})
    except Exception as e:
        return render(request, 'error_page.html', {'message': f"خطا در ایجاد محصول: {str(e)}"})


def success_page(request):
    return render(request, 'success.html', {'message': 'عملیات با موفقیت انجام شد!'})


def error_page(request):
    return render(request, 'error_page.html', {'message': 'عملیات با موفقیت انجام شد!'})


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
