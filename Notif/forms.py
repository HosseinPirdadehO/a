from .models import AdvertisementNotification
from .models import ContentNotification
from .models import ModalNotification
from django import forms
from .models import NotificationSms


class NotificationSmsForm(forms.ModelForm):
    class Meta:
        model = NotificationSms
        fields = ['title', 'content', 'city',
                  'user_group', 'is_selected', 'action']
        labels = {
            'title': 'عنوان اطلاع‌رسانی',
            'content': 'متن اطلاع‌رسانی',
            'city': 'شهر مرتبط',
            'user_group': 'گروه کاربران هدف',
            'is_selected': 'انتخاب شده است؟',
            'action': 'اقدام مرتبط',
        }


class ModalNotificationForm(forms.ModelForm):
    class Meta:
        model = ModalNotification
        fields = ['image', 'link', 'content', 'province',
                  'city', 'individual', 'user_group', 'action']
        labels = {
            'image': 'تصویر اطلاع‌رسانی',
            'link': 'لینک مرتبط',
            'content': 'متن اطلاع‌رسانی',
            'province': 'استان',
            'city': 'شهر',
            'individual': 'نام فرد مشخص‌شده',
            'user_group': 'گروه کاربران هدف',
            'action': 'اقدام مرتبط',
        }


class ContentNotificationForm(forms.ModelForm):
    class Meta:
        model = ContentNotification
        fields = ['image', 'link', 'content', 'province',
                  'city', 'individual', 'user_group', 'action']
        labels = {
            'image': 'تصویر اطلاع‌رسانی',
            'link': 'لینک مرتبط',
            'content': 'متن اطلاع‌رسانی',
            'province': 'استان',
            'city': 'شهر',
            'individual': ' فرد ',
            'user_group': 'گروه کاربران هدف',
            'action': 'اقدام مرتبط',
        }
    help_texts = {
        'image': 'تصویر مرتبط را آپلود کنید',
    }


class AdvertisementNotificationForm(forms.ModelForm):
    class Meta:
        model = AdvertisementNotification
        fields = ['image', 'link', 'content', 'province',
                  'city', 'individual', 'user_group', 'action']
        labels = {
            'image': 'تصویر تبلیغات',
            'link': 'لینک مرتبط',
            'content': 'متن تبلیغات',
            'province': 'استان',
            'city': 'شهر',
            'individual': ' فرد ',
            'user_group': 'گروه کاربران هدف',
            'action': 'اقدام مرتبط',
        }
    help_texts = {
        'image': 'تصویر مرتبط را آپلود کنید',
    }
