from django.db import models


class Product(models.Model):
    SALE_STATUS_CHOICES = [
        ('normal_sale', 'فروش عادی'),
        ('not_for_sale', 'عدم فروش محصول'),
        ('not_displayed', 'عدم نمایش محصول'),
    ]
    OPERATIONS_CHOICES = [
        ('edit_stock', 'ویرایش موجودی'),
        ('edit_price', 'ویرایش قیمت'),
        ('register', 'ثبت'),
    ]

    image = models.ImageField(
        upload_to="product_images/", verbose_name="تصویر اصلی", null=True)
    barcode = models.CharField(
        max_length=100, unique=False, verbose_name="بارکد", null=True)
    name = models.CharField(max_length=255, verbose_name="نام محصول")
    stock = models.IntegerField(verbose_name="موجودی")
    unit = models.CharField(max_length=50, verbose_name="واحد")
    stock_warning = models.IntegerField(verbose_name="هشدار موجودی", null=True)
    category = models.CharField(max_length=255, verbose_name="دسته‌بندی")
    brand = models.CharField(max_length=255, verbose_name="برند")
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت خرید")
    cover_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت روی جلد")
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="قیمت فروش")
    manufacture_date = models.DateField(verbose_name="تاریخ تولید")
    expiration_date = models.DateField(verbose_name="تاریخ انقضا")
    expiration_threshold = models.IntegerField(
        verbose_name="آستانه انقضا", null=True)
    sale_status = models.CharField(
        max_length=20, choices=SALE_STATUS_CHOICES, verbose_name="وضعیت فروش")
    marketer_profit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="سود بازاریاب")
    turnover = models.IntegerField(verbose_name="گردش کالا")
    operations = models.CharField(
        max_length=20, choices=OPERATIONS_CHOICES, verbose_name="عملیات")
    description = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد", null=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_images", verbose_name="محصول"
    )
    image = models.ImageField(
        upload_to="product_extra_images/", verbose_name="تصویر اضافی", null=True)
    alt_text = models.CharField(
        max_length=255, blank=True, verbose_name="متن جایگزین")

    class Meta:
        verbose_name = 'تصویر اضافی محصول'
        verbose_name_plural = 'تصاویر اضافی محصولات'

    def __str__(self):
        return f"تصویر {self.product.name}"
