from django.db import models
from cities_light.models import City, Region
from geopy.geocoders import Nominatim
from django.db import models


class Shopper(models.Model):
    full_name = models.CharField(
        max_length=255, verbose_name="نام و نام خانوادگی")
    store_name = models.CharField(max_length=255, verbose_name="نام فروشگاه")
    contact_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    national_code = models.CharField(
        max_length=10, unique=True, verbose_name="کد ملی")
    status = models.CharField(
        max_length=20,
        choices=[('active', 'فعال'), ('inactive', 'غیرفعال')],
        verbose_name="وضعیت"
    )
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    location = models.TextField(verbose_name="موقعیت")
    shopping_cart = models.TextField(blank=True, verbose_name="سبد خرید")
    financial_limit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0, verbose_name="محدودیت مالی"
    )
    history = models.TextField(blank=True, verbose_name="سابقه")
    notifications = models.TextField(blank=True, verbose_name="نوتیفیکیشن‌ها")
    is_authenticated = models.BooleanField(
        default=False, verbose_name="احراز هویت")
    actions = models.TextField(blank=True, verbose_name="عملیات")

    class Meta:
        verbose_name = "پروفایل خریدار "
        verbose_name_plural = "پروفایل‌ خریدار"

    def __str__(self):
        return self.full_name


class Buyer(models.Model):
    STATUS_CHOICES = [
        ('active', 'فعال'),
        ('inactive', 'غیرفعال'),
    ]

    PAYMENT_LIMIT_CHOICES = [
        ('cash', 'نقد'),
        ('check', 'چک'),
        ('promissory_note', 'سفته'),
        ('Wallet', 'کیف پول'),
        ('Gateway', 'درگاه'),
        ('Cardreader', 'کارتخوان'),
    ]

    OPERATIONS_CHOICES = [
        ('created', 'ایجاد'),
        ('edited', 'ویرایش'),
        ('not_created', 'ایجاد نشده'),
    ]
    OPERATION_CHOICES = [
        ('register', 'ثبت'),
        ('action', 'اقدام'),
        ('edit_stock', 'ویرایش موجودی'),
        ('edit_price', 'ویرایش قیمت'),
        ('normal_sale', 'فروش عادی'),
        ('not_for_sale', 'عدم فروش محصول'),
        ('not_displayed', 'عدم نمایش محصول'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(max_length=10)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    province = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    shopping_cart = models.TextField()
    financial_limit = models.CharField(
        max_length=15, choices=PAYMENT_LIMIT_CHOICES)
    purchase_history = models.TextField()
    messenger = models.CharField(max_length=255)
    authentication = models.BooleanField(default=False)
    operations = models.CharField(
        max_length=12, choices=OPERATIONS_CHOICES, default='register')
    current_location = models.CharField(
        max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'خریدار'
        verbose_name_plural = 'خریدار'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def update_location(self, latitude, longitude):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        self.current_location = location.address
        self.save()


class BuyerCart(models.Model):
    order_number = models.CharField(max_length=50)  # شماره سفارش
    purchase_type = models.CharField(max_length=50)  # نوع خرید
    order_date = models.DateTimeField()  # تاریخ سفارش
    delivery_date = models.DateTimeField()  # تاریخ تحویل
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2)  # مبلغ کل
    settlement_type = models.CharField(
        max_length=50)  # نوع تسویه نیاز به ادیت دارد
    product_name = models.CharField(max_length=100)  # نام محصول
    quantity = models.PositiveIntegerField()  # تعداد
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # فی

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'


class BuyerProduct(models.Model):
    cart = models.ForeignKey(
        BuyerCart, on_delete=models.CASCADE, related_name="products")  # ارجاع به سبد خرید
    product_name = models.CharField(max_length=100)  # نام محصول
    quantity = models.PositiveIntegerField()  # تعداد
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # فی

    class Meta:
        verbose_name = 'خریدار محصول'
        verbose_name_plural = 'خریدار محصول'


class PurchaseHistory(models.Model):
    contact_number = models.CharField(max_length=20)  # شماره تماس
    purchase_type = models.CharField(max_length=50)  # نوع خرید
    order_date = models.DateTimeField()  # تاریخ سفارش
    delivery_date = models.DateTimeField()  # تاریخ تحویل
    settlement_date = models.DateTimeField()  # تاریخ تسویه حساب
    settlement_details = models.TextField()  # اطلاعات تسویه

    class Meta:
        verbose_name = 'تاریخچه خرید'
        verbose_name_plural = 'تاریخچه خرید'


class PurchaseHistoryProduct(models.Model):
    purchase_history = models.ForeignKey(
        PurchaseHistory, on_delete=models.CASCADE, related_name="products")  # ارجاع به سابقه خرید
    product_name = models.CharField(max_length=100)  # نام محصول
    quantity = models.PositiveIntegerField()  # تعداد
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # فی
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2)  # جمع کل

    class Meta:
        verbose_name = 'تاریخچه خرید محصول'
        verbose_name_plural = 'تاریخچه خرید محصول'


class BuyerAuthentication(models.Model):
    contact_number = models.BooleanField(default=False)   # شماره تماس
    national_id = models.BooleanField(default=False)  # کد ملی
    id_card_image = models.ImageField(
        upload_to='auth_documents/id_cards/')  # تصویر کارت ملی
    birth_certificate_image = models.ImageField(
        upload_to='auth_documents/birth_certificates/')  # تصویر شناسنامه
    guarantee_or_check_contract = models.FileField(
        upload_to='auth_documents/contracts/')  # قرارداد ضمانت یا چک

    class Meta:
        verbose_name = 'احراز هویت خریدار'
        verbose_name_plural = 'احراز هویت خریدار'

    def __str__(self):
        return f"Buyer: {self.contact_number} - National ID: {self.national_id}"


# from django.db import models

# class YourModel(models.Model):
#     contact_number = models.CharField(max_length=20)  # شماره تماس
#     national_id = models.CharField(max_length=10, unique=True)  # کد ملی
#     is_verified = models.BooleanField(default=False)  # تایید شد یا خیر

#     def verify(self):
#         # شرط برای بررسی اعتبار شماره تماس و کد ملی
#         if self.contact_number.isdigit() and len(self.national_id) == 10 and self.national_id.isdigit():
#             self.is_verified = True
#         else:
#             self.is_verified = False
#         self.save()


# class Buyer(models.Model):
#     full_name = models.CharField(max_length=255)  # نام و نام خانوادگی
#     store_name = models.CharField(max_length=255, null=True, blank=True)  # نام فروشگاه
#     phone_number = models.CharField(max_length=15)  # شماره تماس
#     national_code = models.CharField(max_length=10, unique=True)  # کد ملی
#     status = models.CharField(max_length=50, choices=[
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#     ])  # وضعیت
#     province = models.CharField(max_length=100)  # استان
#     city = models.CharField(max_length=100)  # شهر
#     location = models.CharField(max_length=255, null=True, blank=True)  # موقعیت
#     shopping_cart = models.TextField(null=True, blank=True, help_text="جزئیات سبد خرید")  # سبد خرید
#     history = models.TextField(null=True, blank=True, help_text="سابقه خرید")  # سابقه
#     messenger = models.CharField(max_length=255, null=True, blank=True, help_text="اطلاعات پیام‌رسان")  # پیام‌رسان
#     authentication = models.BooleanField(default=False, help_text="وضعیت احراز هویت")  # احراز هویت
#     operations = models.TextField(null=True, blank=True)  # عملیات مرتبط

#     def __str__(self):
#         return self.full_name
