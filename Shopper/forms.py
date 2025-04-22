from django import forms
from .models import BuyerAuthentication, BuyerCart, BuyerProduct, PurchaseHistory, PurchaseHistoryProduct, Shopper, Buyer


# class ShopperForm(forms.ModelForm):
#     class Meta:
#         model = Shopper
#         fields = '__all__'
#         labels = {
#             'full_name': 'نام و نام خانوادگی',
#             'store_name': 'نام فروشگاه',
#             'contact_number': 'شماره تماس',
#             'national_code': 'کد ملی',
#             'status': 'وضعیت',
#             'province': 'استان',
#             'city': 'شهر',
#             'location': 'موقعیت',
#             'shopping_cart': 'سبد خرید',
#             'financial_limit': 'محدودیت مالی',
#             'history': 'سابقه',
#             'notifications': 'نوتیفیکیشن‌ها',
#             'is_authenticated': 'احراز هویت',
#             'actions': 'عملیات',
#         }


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'store_name': 'نام فروشگاه',
            'phone_number': 'شماره تماس',
            'national_id': 'کد ملی',
            'status': 'وضعیت',
            'province': 'استان',
            'city': 'شهر',
            'shopping_cart': 'سبد خرید',
            'financial_limit': 'محدودیت مالی',
            'purchase_history': 'سابقه خرید',
            'messenger': 'پیام‌رسان',
            'authentication': 'احراز هویت',
            'operations': 'عملیات',
            'current_location': 'موقعیت فعلی',
            'created_at': 'زمان ایجاد',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # گرفتن اطلاعات کاربر
        super(BuyerForm, self).__init__(*args, **kwargs)

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


# سبد خرید


class BuyerCartForm(forms.ModelForm):
    class Meta:
        model = BuyerCart
        fields = '__all__'
        labels = {
            'order_number': 'شماره سفارش',
            'purchase_type': 'نوع خرید',
            'order_date': 'تاریخ سفارش',
            'delivery_date': 'تاریخ تحویل',
            'total_amount': 'مبلغ کل',
            'settlement_type': 'نوع تسویه',
            'product_name': 'نام محصول',
            'quantity': 'تعداد',
            'unit_price': 'فی',
        }

# خریدار محصول


class BuyerProductForm(forms.ModelForm):
    class Meta:
        model = BuyerProduct
        fields = '__all__'
        labels = {
            'cart': 'سبد خرید',
            'product_name': 'نام محصول',
            'quantity': 'تعداد',
            'unit_price': 'فی',
        }

# تاریخچه خرید


class PurchaseHistoryForm(forms.ModelForm):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'
        labels = {
            'contact_number': 'شماره تماس',
            'purchase_type': 'نوع خرید',
            'order_date': 'تاریخ سفارش',
            'delivery_date': 'تاریخ تحویل',
            'settlement_date': 'تاریخ تسویه حساب',
            'settlement_details': 'اطلاعات تسویه',
        }

# تاریخچه خرید محصول


class PurchaseHistoryProductForm(forms.ModelForm):
    class Meta:
        model = PurchaseHistoryProduct
        fields = '__all__'
        labels = {
            'purchase_history': 'سابقه خرید',
            'product_name': 'نام محصول',
            'quantity': 'تعداد',
            'unit_price': 'فی',
            'total_price': 'جمع کل',
        }

# احراز هویت خریدار


class BuyerAuthenticationForm(forms.ModelForm):
    class Meta:
        model = BuyerAuthentication
        fields = '__all__'
        labels = {
            'contact_number': 'شماره تماس',
            'national_id': 'کد ملی',
            'id_card_image': 'تصویر کارت ملی',
            'birth_certificate_image': 'تصویر شناسنامه',
            'guarantee_or_check_contract': 'قرارداد ضمانت یا چک',
        }
