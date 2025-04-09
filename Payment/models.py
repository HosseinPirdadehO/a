from django.db import models

# مالی اصلی


class Payment(models.Model):
    OPERATIONS_CHOICES = [
        ('created', 'ایجاد'),
        ('edited', 'ویرایش'),
        ('not_created', 'ایجاد نشده'),
    ]

    PAYMENT_LIMIT_CHOICES = [
        ('cash', 'نقد'),
        ('check', 'چک'),
        ('promissory_note', 'سفته'),
        ('Wallet', 'کیف پول'),
        ('Gateway', 'درگاه'),
        ('Cardreader', 'کارتخوان'),
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
        max_digits=15, decimal_places=2, default=0.0, choices=PAYMENT_LIMIT_CHOICES)  # محدودیت مالی
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
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(
        max_length=50, verbose_name="نام خانوادگی")
    role = models.CharField(max_length=50, verbose_name="نقش")
    contact_number = models.CharField(
        max_length=20, verbose_name="شماره تماس")
    national_id = models.CharField(
        max_length=10, unique=True, verbose_name="کد ملی")
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50, verbose_name="شهر")
    status = models.CharField(
        max_length=20,
        choices=[('active', 'فعال'), ('inactive', 'غیرفعال')],
        verbose_name="وضعیت"
    )
    wallet_balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.0, verbose_name="موجودی کیف پول"
    )
    notifications = models.TextField(
        blank=True, verbose_name="نوتیفیکیشن‌ها")
    actions = models.TextField(blank=True, verbose_name="عملیات")

    class Meta:
        verbose_name = 'مالی بازاریاب'
        verbose_name_plural = 'مالی بازاریاب‌ها'

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
    PAYMENT_LIMIT_CHOICES = [
        ('cash', 'نقد'),
        ('check', 'چک'),
        ('promissory_note', 'سفته'),
        ('Wallet', 'کیف پول'),
        ('Gateway', 'درگاه'),
        ('Cardreader', 'کارتخوان'),
    ]

    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="settlements", verbose_name=" مالی ", null=True)
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
        max_digits=10, decimal_places=2, verbose_name="محدودیت مالی", choices=PAYMENT_LIMIT_CHOICES)
    history = models.TextField(blank=True, verbose_name="سابقه")
    messenger = models.CharField(
        max_length=50, blank=True, verbose_name="پیام رسان")

    class Meta:
        verbose_name = 'مالی خریدار'
        verbose_name_plural = 'مالی خریدار'

    def __str__(self):
        return self.full_name

# مالی خریدار تسویه شده


class FinanciallySettled(models.Model):
    PAYMENT_LIMIT_CHOICES = [
        ('cash', 'نقد'),
        ('check', 'چک'),
        ('promissory_note', 'سفته'),
        ('Wallet', 'کیف پول'),
        ('Gateway', 'درگاه'),
        ('Cardreader', 'کارتخوان'),
    ]
    order_number = models.CharField(max_length=50, verbose_name="شماره سفارش")
    purchase_type = models.CharField(max_length=50, verbose_name="نوع خرید")
    product_items = models.TextField(verbose_name="اقلام کالایی")
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="مبلغ کل")
    order_date = models.DateField(verbose_name="تاریخ سفارش")
    delivery_date = models.DateField(verbose_name="تاریخ تحویل",)
    settlement_date = models.DateField(verbose_name=" تاریخ تصویه حساب")
    settlement_info = models.TextField(
        verbose_name="اطلاعات تسویه", choices=PAYMENT_LIMIT_CHOICES)
    document = models.FileField(upload_to='documents/', verbose_name="سند")
    operation = models.CharField(max_length=50, verbose_name="عملیات")
    product_name = models.CharField(max_length=100, verbose_name="نام محصول")
    quantity = models.IntegerField(verbose_name="تعداد")
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="فی")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="جمع مبلغ")
    settlement_type = models.CharField(max_length=50, verbose_name="نوع تسویه")
    referred_to = models.CharField(max_length=50, verbose_name="ارجاع به ")
    explainer_name = models.CharField(
        max_length=50, verbose_name="نام توضیح کننده")

    class Meta:
        verbose_name = 'مالی خریدار تسویه شده'
        verbose_name_plural = 'مالی خریدار تسویه شده'

    def __str__(self):
        return f"Order {self.order_number} - {self.product_name}"

# درخواست تسویه زمان دار برای چک یا سفته


class RequestActivation(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name="نام و نام خانوادگی")
    store_name = models.CharField(max_length=100, verbose_name="نام فروشگاه")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    national_id = models.CharField(max_length=10, verbose_name="کد ملی")
    province = models.CharField(max_length=50, verbose_name="استان")
    location = models.TextField(verbose_name="لوکیشن")
    request = models.TextField(verbose_name="درخواست")
    registration_date = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت")
    referred_to = models.CharField(max_length=100, verbose_name="ارجاع به")
    action = models.TextField(verbose_name="اقدام")

    class Meta:
        verbose_name = 'ثبت درخواست'
        verbose_name_plural = 'ثبت درخواست‌ها'

    def __str__(self):
        return f"{self.full_name} - {self.store_name}"
