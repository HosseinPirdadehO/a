from django.core.paginator import Paginator
from django.contrib import messages
from .forms import BrandForm
from .models import Brand
from .forms import CategoryForm
from .models import Category
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Brand, Category
from .Serializers import BrandSerializer, CategorySerializer

# Create your views here.


class CategoryViewSet(ViewSet):
    def list(self, request):
        try:
            categories = Category.objects.all()  # دریافت همه دسته‌بندی‌ها
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "خطایی رخ داده است", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(
                {"error": "دسته‌بندی مورد نظر یافت نشد"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "خطایی رخ داده است", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


#


def category_list(request):
    try:
        categories = Category.objects.all()  # دریافت تمام دسته‌بندی‌ها
        return render(request, 'category_list.html', {'categories': categories})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در دریافت دسته‌بندی‌ها رخ داده است.', 'details': str(e)})


def create_category(request):
    try:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('category_list')  # بازگشت به لیست دسته‌بندی‌ها
        else:
            form = CategoryForm()
        return render(request, 'category_form.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در ایجاد دسته‌بندی رخ داده است.', 'details': str(e)})


def edit_category(request, pk):
    try:
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('category_list')  # بازگشت به لیست دسته‌بندی‌ها
        else:
            form = CategoryForm(instance=category)
        return render(request, 'category_form.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در ویرایش دسته‌بندی رخ داده است.', 'details': str(e)})


def delete_category(request, pk):
    try:
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            category.delete()
            return redirect('category_list')  # بازگشت به لیست دسته‌بندی‌ها
        return render(request, 'confirm_delete.html', {'object': category})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در حذف دسته‌بندی رخ داده است.', 'details': str(e)})


def create_category(request):
    try:
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'دسته‌بندی با موفقیت ایجاد شد.')
                return redirect('category_list')
        else:
            form = CategoryForm()
        return render(request, 'category_form.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در ایجاد دسته‌بندی رخ داده است.', 'details': str(e)})


#


def brand_list(request):
    try:
        brands = Brand.objects.all()  # دریافت تمام برندها
        return render(request, 'brand_list.html', {'brands': brands})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در دریافت برندها رخ داده است.', 'details': str(e)})


def create_brand(request):
    try:
        if request.method == 'POST':
            form = BrandForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('brand_list')  # بازگشت به لیست برندها
        else:
            form = BrandForm()
        return render(request, 'brand_form.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در ایجاد برند رخ داده است.', 'details': str(e)})


def edit_brand(request, pk):
    try:
        brand = get_object_or_404(Brand, pk=pk)
        if request.method == 'POST':
            form = BrandForm(request.POST, request.FILES, instance=brand)
            if form.is_valid():
                form.save()
                return redirect('brand_list')  # بازگشت به لیست برندها
        else:
            form = BrandForm(instance=brand)
        return render(request, 'brand_form.html', {'form': form})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در ویرایش برند رخ داده است.', 'details': str(e)})


def delete_brand(request, pk):
    try:
        brand = get_object_or_404(Brand, pk=pk)
        if request.method == 'POST':
            brand.delete()
            return redirect('brand_list')  # بازگشت به لیست برندها
        return render(request, 'confirm_delete.html', {'object': brand})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در حذف برند رخ داده است.', 'details': str(e)})


#


def category_list(request):
    try:
        categories = Category.objects.all()
        paginator = Paginator(categories, 10)  # 10 مورد در هر صفحه
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'category_list.html', {'page_obj': page_obj})
    except Exception as e:
        return render(request, 'error.html', {'message': 'خطایی در دریافت دسته‌بندی‌ها رخ داده است.', 'details': str(e)})


#
