from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'image', 'name', 'stock', 'unit', 'category', 'brand',
            'purchase_price', 'cover_price', 'sale_price',
            'manufacture_date', 'expiration_date', 'sale_status',
            'marketer_profit', 'turnover', 'operations', 'description'
        ]
        labels = {
            'image': 'تصویر محصول',
            'name': 'نام محصول',
            'stock': 'موجودی',
            'unit': 'واحد',
            'category': 'دسته‌بندی',
            'brand': 'برند',
            'purchase_price': 'قیمت خرید',
            'cover_price': 'قیمت روی جلد',
            'sale_price': 'قیمت فروش',
            'manufacture_date': 'تاریخ تولید',
            'expiration_date': 'تاریخ انقضا',
            'sale_status': 'وضعیت فروش',
            'marketer_profit': 'سود بازاریاب',
            'turnover': 'گردش کالا',
            'operations': 'عملیات',
            'description': 'توضیحات',
        }
