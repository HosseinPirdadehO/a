from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from cities_light.models import City, Region


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('buyer', 'خریدار'),
        ('seller', 'فروشنده'),
        ('marketer', 'بازاریاب'),
    ]

    OPERATIONS_CHOICES = [
        ('created', 'ایجاد'),
        ('edited', 'ویرایش'),
        ('not_created', 'ایجاد نشده'),
    ]

    STATUS_CHOICES = [
        ('active', 'فعال'),
        ('inactive', 'غیرفعال'),
    ]

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, verbose_name='نقش')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')
    national_id = models.CharField(max_length=10, verbose_name='کد ملی')
    province = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, verbose_name='استان')
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, verbose_name='شهر')
    wallet_status = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default='0',
        verbose_name='وضعیت کیف پول'
    )
    messenger = models.CharField(max_length=255, verbose_name='اطلاع رسانی')
    operations = models.CharField(
        max_length=12, choices=OPERATIONS_CHOICES, verbose_name='عملیات')
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, verbose_name='وضعیت')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'اکانت'
        verbose_name_plural = 'اکانت‌ها'
