from django.contrib import admin
from .models import Buyer, BuyerCart, BuyerProduct, PurchaseHistory, PurchaseHistoryProduct, BuyerAuthentication, Shopper
from django.utils.html import format_html
from django.contrib import admin


# Register your models here.


@admin.register(Shopper)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'store_name', 'contact_number', 'national_code', 'status',
        'province', 'city', 'financial_limit', 'is_authenticated'
    )
    list_filter = ('status', 'province', 'city', 'is_authenticated')
    search_fields = ('full_name', 'store_name',
                     'contact_number', 'national_code')
    ordering = ('-financial_limit',)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'store_name', 'phone_number',
                    'status', 'province', 'city', 'financial_limit', 'authentication')
    search_fields = ('first_name', 'last_name', 'store_name',
                     'phone_number', 'national_id')
    list_filter = ('status', 'province', 'city',
                   'financial_limit')  # قابلیت فیلترگذاری
    readonly_fields = ('current_location',)  # فقط خواندنی برای مکان فعلی
    actions = ['mark_as_authenticated',
               'mark_as_unauthenticated']  # اکشن‌های سفارشی

    def mark_as_authenticated(self, request, queryset):
        queryset.update(authentication=True)
        self.message_user(request, "خریداران انتخاب‌شده تأیید شدند.")
    mark_as_authenticated.short_description = "تأیید خریداران انتخاب‌شده"

    def mark_as_unauthenticated(self, request, queryset):
        queryset.update(authentication=False)
        self.message_user(request, "تأیید خریداران انتخاب‌شده لغو شد.")
    mark_as_unauthenticated.short_description = "لغو تأیید خریداران انتخاب‌شده"


@admin.register(BuyerCart)
class BuyerCartAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'purchase_type', 'order_date',
                    'delivery_date', 'total_amount', 'settlement_type')
    search_fields = ('order_number', 'purchase_type')
    list_filter = ('purchase_type', 'order_date', 'delivery_date')


@admin.register(BuyerProduct)
class BuyerProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product_name', 'quantity', 'unit_price')
    search_fields = ('product_name',)


@admin.register(PurchaseHistory)
class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ('contact_number', 'purchase_type',
                    'order_date', 'delivery_date', 'settlement_date')
    search_fields = ('contact_number', 'purchase_type')
    list_filter = ('order_date', 'delivery_date', 'settlement_date')


@admin.register(PurchaseHistoryProduct)
class PurchaseHistoryProductAdmin(admin.ModelAdmin):
    list_display = ('purchase_history', 'product_name',
                    'quantity', 'unit_price', 'total_price')
    search_fields = ('product_name',)


@admin.register(BuyerAuthentication)
class BuyerAuthenticationAdmin(admin.ModelAdmin):
    list_display = ('contact_number', 'national_id', 'id_card_image_preview',
                    'birth_certificate_image_preview', 'guarantee_or_check_contract_preview')
    search_fields = ('contact_number', 'national_id')
    readonly_fields = ('id_card_image_preview', 'birth_certificate_image_preview',
                       'guarantee_or_check_contract_preview')  # پیش‌نمایش تصاویر

    def id_card_image_preview(self, obj):
        if obj.id_card_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.id_card_image.url)
        return "بدون تصویر"
    id_card_image_preview.short_description = 'پیش‌نمایش کارت ملی'

    def birth_certificate_image_preview(self, obj):
        if obj.birth_certificate_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.birth_certificate_image.url)
        return "بدون تصویر"
    birth_certificate_image_preview.short_description = 'پیش‌نمایش شناسنامه'

    def guarantee_or_check_contract_preview(self, obj):
        if obj.guarantee_or_check_contract:
            return format_html('<a href="{}" target="_blank">دانلود قرارداد</a>', obj.guarantee_or_check_contract.url)
        return "بدون فایل"
    guarantee_or_check_contract_preview.short_description = 'پیش‌نمایش قرارداد'
