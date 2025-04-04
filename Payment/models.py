from django.db import models

# مالی اصلی


class Payment(models.Model):
    OPERATIONS_CHOICES = [
        ('register', 'ثبت'),
        ('action', 'اقدام'),
        ('edit_stock', 'ویرایش موجودی'),
        ('edit_price', 'ویرایش قیمت'),
        ('normal_sale', 'فروش عادی'),
        ('not_for_sale', 'عدم فروش محصول'),
        ('not_displayed', 'عدم نمایش محصول'),
    ]
    first_name = models.CharField(max_length=50)  # نام
    last_name = models.CharField(max_length=50)  # نام خانوادگی
    store_name = models.CharField(max_length=100)  # نام فروشگاه
    contact_number = models.CharField(max_length=20)  # شماره تماس
    national_id = models.CharField(max_length=10, unique=True)  # کد ملی
    province = models.CharField(max_length=50)  # استان
    city = models.CharField(max_length=50)  # شهر
    location = models.CharField(max_length=255)  # لوکیشن
    debt = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0)  # بدهی
    financial_limit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0)  # محدودیت مالی
    history = models.TextField(blank=True)  # سابقه
    notifications = models.TextField(blank=True)  # نوتیفیکیشن‌ها
    operations = models.CharField(
        max_length=20, choices=OPERATIONS_CHOICES, default='register')

    class Meta:
        verbose_name = ' مالی اصلی'
        verbose_name_plural = ' مالی اصلی'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.store_name}"

# مالی بازاریاب


class MarketerPayment(models.Model):
    first_name = models.CharField(max_length=50)  # نام
    last_name = models.CharField(max_length=50)  # نام خانوادگی
    role = models.CharField(max_length=50)  # نقش
    contact_number = models.CharField(max_length=20)  # شماره تماس
    national_id = models.CharField(max_length=10, unique=True)  # کد ملی
    province = models.CharField(max_length=50)  # استان
    city = models.CharField(max_length=50)  # شهر
    status = models.CharField(max_length=20, choices=[(
        'active', 'فعال'), ('inactive', 'غیرفعال')])  # وضعیت
    wallet_balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0)  # کیف پول
    notifications = models.TextField(blank=True)  # نوتیفیکیشن‌ها
    actions = models.TextField(blank=True)  # عملیات

    class Meta:
        verbose_name = 'مالی بازاریاب'
        verbose_name_plural = 'مالی بازاریاب'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


# NeedForAction(models.Model):  # برای بازاریاب نیاز به اقدام
    requires_action = models.BooleanField(
        default=False)  # نیاز به اقدام (انتخاب شده)
    total_paid_profit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0)  # مجموع سود پرداخت شده
    payment_document = models.ImageField(
        upload_to='marketer_documents/payments/', blank=True)  # سند پرداخت
    action_details = models.TextField(blank=True)  # جزئیات اقدام


class HistoryMarketerPayment(models.Model):  # سابقه بازاریاب
    history = models.CharField(max_length=255, verbose_name="سابقه")
    is_selected = models.BooleanField(default=False, verbose_name="انتخاب شده")
    total_paid_profit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="مجموع سود پرداخت شده")
    document = models.FileField(upload_to='documents/', verbose_name="سند")
    more_details = models.TextField(blank=True, verbose_name="نمایش بیشتر")
    payment_date = models.DateField(verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = ' سابقه بازاریاب  '
        verbose_name_plural = ' سابقه بازاریاب  '

    def __str__(self):
        return f"{self.history} - {'انتخاب شده' if self.is_selected else 'انتخاب نشده'}"


class ProductPayment(models.Model):  # سابقه محصول
    image = models.ImageField(
        upload_to='Payment_images/', null=True, blank=True)
    product_name = models.CharField(max_length=255, verbose_name="نام محصول")
    stock = models.IntegerField(verbose_name="موجودی")
    unit = models.CharField(max_length=50, verbose_name="واحد")
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت خرید")
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت فروش")
    cover_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت روی جلد")
    operation = models.TextField(blank=True, verbose_name="عملیات")
    profit_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="درصد سود")
    inventory_turnover = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="گردش کالا")
    sales_history = models.TextField(blank=True, verbose_name="سابقه فروش")
    actions = models.TextField(blank=True)

    class Meta:
        verbose_name = 'سابقه محصول'
        verbose_name_plural = 'سابقه محصول'

    def __str__(self):
        return self.product_name


# مالی خریدار


class BuyerPayment(models.Model):
    full_name = models.CharField(
        max_length=255, verbose_name="نام و نام خانوادگی")
    store_name = models.CharField(max_length=255, verbose_name="نام فروشگاه")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    location = models.TextField(verbose_name="لوکیشن")
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="بدهی")
    financial_limit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="محدودیت مالی")
    history = models.TextField(blank=True, verbose_name="سابقه")
    messenger = models.CharField(
        max_length=50, blank=True, verbose_name="پیام رسان")

    class Meta:
        verbose_name = 'مالی خریدار'
        verbose_name_plural = 'مالی خریدار'

    def __str__(self):
        return self.full_name
