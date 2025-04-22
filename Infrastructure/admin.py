from django.contrib import admin
from .models import Category, Brand
# Register your models here.
# تنظیمات ادمین برای مدل دسته‌بندی


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # نمایش فیلدها در لیست

    search_fields = ('name', 'description')
    list_filter = ('name',)  # فیلتر کردن بر اساس نام
    ordering = ('id',)  # مرتب‌سازی بر اساس شناسه

# تنظیمات ادمین برای مدل برند


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',
                    'image')  # نمایش فیلدها در لیست

    search_fields = ('name', 'description')
    list_filter = ('name',)  # فیلتر کردن بر اساس نام
    ordering = ('id',)  # مرتب‌سازی بر اساس شناسه
