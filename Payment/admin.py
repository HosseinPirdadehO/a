from .models import BuyerPayment
from django.contrib import admin
from .models import Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment
from django.utils.html import format_html

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'store_name',
                    'contact_number', 'province', 'city', 'debt', 'financial_limit')
    search_fields = ('first_name', 'last_name', 'store_name',
                     'national_id', 'contact_number')
    list_filter = ('province', 'city')  # فیلترگذاری بر اساس استان و شهر
    readonly_fields = ('debt',)  # فیلدی که فقط قابل مشاهده است


@admin.register(MarketerPayment)
class MarketerPaymentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'contact_number',
                    'province', 'city', 'status', 'wallet_balance')
    # فیلترگذاری بر اساس وضعیت و موقعیت جغرافیایی
    list_filter = ('status', 'province', 'city')
    search_fields = ('first_name', 'last_name', 'role',
                     'contact_number', 'national_id')
    actions = ['mark_as_active', 'mark_as_inactive']  # اکشن‌های سفارشی

    def mark_as_active(self, request, queryset):
        queryset.update(status='active')
        self.message_user(request, "بازاریاب‌های انتخاب‌شده فعال شدند.")
    mark_as_active.short_description = "فعال کردن بازاریاب‌های انتخاب‌شده"

    def mark_as_inactive(self, request, queryset):
        queryset.update(status='inactive')
        self.message_user(request, "بازاریاب‌های انتخاب‌شده غیرفعال شدند.")
    mark_as_inactive.short_description = "غیرفعال کردن بازاریاب‌های انتخاب‌شده"


@admin.register(HistoryMarketerPayment)
class HistoryMarketerPaymentAdmin(admin.ModelAdmin):
    list_display = ('history', 'is_selected', 'total_paid_profit',
                    'payment_date', 'document_preview')
    # فیلترگذاری بر اساس تاریخ پرداخت
    list_filter = ('is_selected', 'payment_date')
    search_fields = ('history', 'more_details')

    def document_preview(self, obj):
        if obj.document:
            return format_html('<a href="{}" target="_blank">مشاهده سند</a>', obj.document.url)
        return "بدون سند"
    document_preview.short_description = "پیش‌نمایش سند"


@admin.register(ProductPayment)
class ProductPaymentAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'stock', 'unit', 'purchase_price',
                    'sale_price', 'cover_price', 'profit_percentage', 'inventory_turnover')
    search_fields = ('product_name',)
    # فیلترگذاری بر اساس گردش کالا و درصد سود
    list_filter = ('profit_percentage', 'inventory_turnover')


@admin.register(BuyerPayment)
class BuyerPaymentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'store_name', 'phone_number',
                    'province', 'city', 'debt', 'financial_limit')
    list_filter = ('province', 'city', 'debt')
    search_fields = ('full_name', 'store_name',
                     'phone_number', 'national_code')
    ordering = ('-debt',)  # مرتب‌سازی بر اساس بدهی (نزولی)
