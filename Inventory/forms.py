# from django import forms
# from .models import InventoryItem, InventoryHistory, Supplier


# class InventoryItemForm(forms.ModelForm):
#     class Meta:
#         model = InventoryItem
#         fields = ['product', 'quantity', 'location', 'purchase_price',
#                   'expiration_date', 'date_added', 'status', 'supplier', 'description']


# class InventoryHistoryForm(forms.ModelForm):
#     class Meta:
#         model = InventoryHistory
#         fields = ['inventory_item', 'change_quantity', 'date_changed', 'note']


# class SupplierForm(forms.ModelForm):
#     class Meta:
#         model = Supplier
#         fields = ['name', 'contact_info']


#
from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        labels = {
            'image': 'تصویر',
            'product_name': 'نام محصول',
            'stock': 'موجودی',
            'unit': 'واحد',
            'stock_alert': 'هشدار موجودی',
            'category': 'دسته‌بندی',
            'brand': 'برند',
            'purchase_price': 'قیمت خرید',
            'cover_price': 'قیمت پوشش',
            'sale_price': 'قیمت فروش',
            'manufacture_date': 'تاریخ تولید',
            'expiry_date': 'تاریخ انقضا',
            'expiry_threshold': 'آستانه انقضا (روز)',
            'sale_status': 'وضعیت فروش',
            'sale_range': 'دامنه فروش',
            'marketer_profit': 'سود بازاریاب',
            'turnover': 'گردش مالی',
            'operations': 'عملیات',
            'description': 'توضیحات',
        }
