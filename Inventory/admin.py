from django.contrib import admin
from .models import Inventory
from django.utils.html import format_html

# Register your models here.


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'stock', 'unit', 'category', 'brand',
                    'sale_status', 'sale_price', 'expiry_date', 'image_preview')
    # قابلیت جستجو براساس نام محصول، دسته‌بندی و برند
    search_fields = ('product_name', 'category', 'brand')
    # فیلترگذاری براساس وضعیت فروش، دسته‌بندی و برند
    list_filter = ('sale_status', 'category', 'brand')
    # فقط قابل‌مشاهده بودن پیش‌نمایش تصویر
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('اطلاعات محصول', {
            'fields': ('product_name', 'stock', 'unit', 'category', 'brand', 'sale_status', 'sale_price')
        }),
        ('اطلاعات مالی', {
            'fields': ('purchase_price', 'cover_price', 'marketer_profit', 'turnover')
        }),
        ('تاریخ‌ها', {
            'fields': ('manufacture_date', 'expiry_date', 'expiry_threshold')
        }),
        ('جزئیات بیشتر', {
            'fields': ('operations', 'description', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "بدون تصویر"
    image_preview.short_description = 'پیش‌نمایش تصویر'
