from .models import RequestActivation
from .models import FinanciallySettled
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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # گرفتن اطلاعات کاربر
        super(FinanciallySettledForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'چک'),
                ('promissory_note', 'سفته'),
                ('Wallet', 'کیف پول'),
                ('Gateway', 'درگاه'),
            ]

            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'کیف پول'),
                ('promissory_note', 'درگاه'),
            ]

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # گرفتن اطلاعات کاربر
        super(FinanciallySettledForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'چک'),
                ('promissory_note', 'سفته'),
                ('Wallet', 'کیف پول'),
                ('Gateway', 'درگاه'),
            ]

            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'کیف پول'),
                ('promissory_note', 'درگاه'),
            ]


class FinanciallySettledForm(forms.ModelForm):
    class Meta:
        model = FinanciallySettled
        fields = '__all__'  # نمایش تمام فیلدهای مدل در فرم
        labels = {
            'order_number': 'شماره سفارش',
            'purchase_type': 'نوع خرید',
            'product_items': 'اقلام کالایی',
            'total_amount': 'مبلغ کل',
            'order_date': 'تاریخ سفارش',
            'delivery_date': 'تاریخ تحویل',
            'settlement_date': 'تاریخ تصویه حساب',
            'settlement_info': 'اطلاعات تسویه',
            'document': 'سند',
            'operation': 'عملیات',
            'product_name': 'نام محصول',
            'quantity': 'تعداد',
            'unit_price': 'فی',
            'total_price': 'جمع مبلغ',
            'settlement_type': 'نوع تسویه',
            'referred_to': 'ارجاع به',
            'explainer_name': 'نام توضیح کننده',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # گرفتن اطلاعات کاربر
        super(FinanciallySettledForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'چک'),
                ('promissory_note', 'سفته'),
                ('Wallet', 'کیف پول'),
                ('Gateway', 'درگاه'),
            ]

            self.fields['settlement_info'].choices = [
                ('cash', 'نقد'),
                ('check', 'کیف پول'),
                ('promissory_note', 'درگاه'),
            ]


# درخواست تسویه زمان دار


class RequestActivationForm(forms.ModelForm):
    class Meta:
        model = RequestActivation
        fields = '__all__'
        widgets = {
            'location': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            'request': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
            'action': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }
