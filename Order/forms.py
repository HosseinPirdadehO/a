from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'buyer': 'خریدار',
            'order_date': 'تاریخ سفارش',
            'order_number': 'شماره سفارش',
            'delivery_date': 'تاریخ تحویل',
            'delivery_location': 'محل تحویل',
            'product_id': 'شناسه محصول',
            'product_name': 'نام محصول',
            'quantity': 'تعداد',
            'price': 'قیمت',
            'discount': 'تخفیف',
            'total_price': 'قیمت کل',
            'payment_method': 'روش پرداخت',
            'order_method': 'روش سفارش',
            'description': 'توضیحات',
            'total_amount': 'جمع مبلغ',
            'total_discount': 'جمع تخفیف',
            'shipping_cost': 'هزینه حمل‌و‌نقل',
            'grand_total': 'جمع کل',
            'order_code': 'کد سفارش'
        }
