# from django import forms
# from django.core.validators import MinValueValidator, RegexValidator
# from .models import User


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'role',
#             'phone_number',
#             'national_id',
#             'province',
#             'city',
#             'wallet_status',
#             'messenger',
#             'operations',
#             'status',
#         ]
#         labels = {
#             'first_name': 'نام',
#             'last_name': 'نام خانوادگی',
#             'role': 'نقش',
#             'phone_number': 'شماره تماس',
#             'national_id': 'کد ملی',
#             'province': 'استان',
#             'city': 'شهر',
#             'wallet_status': 'وضعیت کیف پول',
#             'messenger': 'پیام رسان',
#             'operations': 'عملیات',
#             'status': 'وضعیت',
#             'current_location': 'موقعیت کنونی',
#         }
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'role': forms.Select(attrs={'class': 'form-control'}),
#             'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'national_id': forms.TextInput(attrs={'class': 'form-control'}),
#             'province': forms.Select(attrs={'class': 'form-control'}),
#             'city': forms.Select(attrs={'class': 'form-control'}),
#             'wallet_status': forms.NumberInput(attrs={'class': 'form-control'}),
#             'messenger': forms.TextInput(attrs={'class': 'form-control'}),
#             'operations': forms.Select(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

#     phone_number = forms.CharField(
#         validators=[RegexValidator(
#             r'^\+?1?\d{9,15}$', 'شماره تماس باید به شکل درست وارد شود (مثال: +1234567890).')]
#     )

#     national_id = forms.CharField(
#         validators=[RegexValidator(
#             r'^\d{10}$', 'کد ملی باید شامل 10 رقم باشد.')]
#     )

#     wallet_status = forms.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         validators=[MinValueValidator(0)],
#         widget=forms.NumberInput(attrs={'class': 'form-control'}),
#         help_text='وضعیت کیف پول باید عددی مثبت باشد.'
#     )

#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if not phone_number.startswith('+98'):
#             raise forms.ValidationError(
#                 'شماره تماس باید با کد کشور ایران (+98) شروع شود.')
#         return phone_number

#     def clean_national_id(self):
#         national_id = self.cleaned_data.get('national_id')
#         # افزودن ولیدیشن سفارشی برای کد ملی (در صورت نیاز)
#         # مثلاً بررسی رقم کنترلی کد ملی
#         return national_id

#     def clean_wallet_status(self):
#         wallet_status = self.cleaned_data.get('wallet_status')
#         if wallet_status < 0:
#             raise forms.ValidationError('وضعیت کیف پول نمی‌تواند منفی باشد.')
#         return wallet_status
