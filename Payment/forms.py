from .models import BuyerPayment
from .models import ProductPayment
from .models import MarketerPayment
from django import forms
from .models import Payment

# مالی اصلی


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'first_name', 'last_name', 'store_name', 'contact_number',
            'national_id', 'province', 'city', 'location', 'debt',
            'financial_limit', 'history', 'notifications'
        ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'store_name': 'نام فروشگاه',
            'contact_number': 'شماره تماس',
            'national_id': 'کد ملی',
            'province': 'استان',
            'city': 'شهر',
            'location': 'لوکیشن',
            'debt': 'بدهی',
            'financial_limit': 'محدودیت مالی',
            'history': 'سابقه',
            'notifications': 'نوتیفیکیشن‌ها'
        }

# مالی بازاریاب


class MarketerPaymentForm(forms.ModelForm):
    class Meta:
        model = MarketerPayment
        fields = [
            'first_name', 'last_name', 'role', 'contact_number', 'national_id',
            'province', 'city', 'status', 'wallet_balance', 'notifications', 'actions'
        ]
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'role': 'نقش',
            'contact_number': 'شماره تماس',
            'national_id': 'کد ملی',
            'province': 'استان',
            'city': 'شهر',
            'status': 'وضعیت',
            'wallet_balance': 'موجودی کیف پول',
            'notifications': 'نوتیفیکیشن‌ها',
            'actions': 'عملیات'
        }

# مالی محصول


class ProductPaymentForm(forms.ModelForm):
    class Meta:
        model = ProductPayment
        fields = [
            'image', 'product_name', 'stock', 'unit', 'purchase_price',
            'sale_price', 'cover_price', 'operation', 'profit_percentage',
            'inventory_turnover', 'sales_history', 'actions'
        ]
        labels = {
            'image': 'تصویر محصول',
            'product_name': 'نام محصول',
            'stock': 'موجودی',
            'unit': 'واحد',
            'purchase_price': 'قیمت خرید',
            'sale_price': 'قیمت فروش',
            'cover_price': 'قیمت روی جلد',
            'operation': 'عملیات',
            'profit_percentage': 'درصد سود',
            'inventory_turnover': 'گردش کالا',
            'sales_history': 'سابقه فروش',
            'actions': 'عملیات'
        }

# مالی خریدار


class BuyerPaymentForm(forms.ModelForm):
    class Meta:
        model = BuyerPayment
        fields = [
            'full_name', 'store_name', 'phone_number', 'national_code',
            'province', 'city', 'location', 'debt', 'financial_limit',
            'history', 'messenger'
        ]
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'store_name': 'نام فروشگاه',
            'phone_number': 'شماره تماس',
            'national_code': 'کد ملی',
            'province': 'استان',
            'city': 'شهر',
            'location': 'لوکیشن',
            'debt': 'بدهی',
            'financial_limit': 'محدودیت مالی',
            'history': 'سابقه',
            'messenger': 'پیام‌رسان'
        }
