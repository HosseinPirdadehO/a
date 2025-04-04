from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'stock', 'unit',
                    'sale_price', 'sale_status', 'expiration_date', 'image_preview')
    # قابلیت جستجو بر اساس نام، دسته‌بندی و برند
    search_fields = ('name', 'category', 'brand')
    # فیلترگذاری براساس دسته‌بندی، برند، وضعیت فروش و تاریخ انقضا
    list_filter = ('category', 'brand', 'sale_status', 'expiration_date')
    readonly_fields = ('image_preview',)  # نمایش فقط‌خواندنی تصویر در فرم
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'image', 'image_preview', 'category', 'brand')
        }),
        ('اطلاعات مالی', {
            'fields': ('purchase_price', 'cover_price', 'sale_price', 'marketer_profit', 'turnover')
        }),
        ('موجودی و وضعیت', {
            'fields': ('stock', 'unit', 'sale_status', 'expiration_date', 'manufacture_date')
        }),
        ('سایر جزئیات', {
            'fields': ('operations', 'description', 'created_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "بدون تصویر"
    image_preview.short_description = 'پیش‌نمایش تصویر'
