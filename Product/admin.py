from django.utils.html import mark_safe
from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'stock', 'unit',
                    'sale_price', 'sale_status', 'expiration_date', 'image_preview')
    readonly_fields = ('created_at', 'image_preview')
    search_fields = ('name', 'category', 'brand')

    list_filter = ('category', 'brand', 'sale_status', 'expiration_date')
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

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.main_image.url)
        return "بدون تصویر"
    main_image_preview.short_description = "پیش‌نمایش تصویر اصلی"

    def ProductImage(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.main_image.url)
        return "بدون تصویر"
    ProductImage.short_description = "پیش‌نمایش تصویر اضافی"

    def barcode_image(self, obj):
        return mark_safe(f'<img src="/media/{obj.barcode}" width="100" />')
    barcode_image.short_description = "بارکد"
