from rest_framework import serializers
from .models import Category, Brand

# سریال‌ساز برای مدل دسته‌بندی


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # فیلدهایی که می‌خواهید در API نمایش داده شوند
        fields = ['id', 'name', 'description']
        extra_kwargs = {
            'name': {'label': 'نام دسته‌بندی'},
            'description': {'label': 'توضیحات دسته‌بندی'},
        }

# سریال‌ساز برای مدل برند


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        # فیلدهایی که می‌خواهید در API نمایش داده شوند
        fields = ['id', 'name', 'description', 'image']
        extra_kwargs = {
            'name': {'label': 'نام برند'},
            'description': {'label': 'توضیحات برند'},
            'image': {'label': 'تصویر برند'},
        }
