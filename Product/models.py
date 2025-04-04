from django.db import models


class Product(models.Model):
    OPERATIONS_CHOICES = [
        ('register', 'ثبت'),
        ('action', 'اقدام'),
        ('edit_stock', 'ویرایش موجودی'),
        ('edit_price', 'ویرایش قیمت'),
        ('normal_sale', 'فروش عادی'),
        ('not_for_sale', 'عدم فروش محصول'),
        ('not_displayed', 'عدم نمایش محصول'),
    ]
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    unit = models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateField()
    expiration_date = models.DateField()
    sale_status = models.CharField(max_length=50)
    marketer_profit = models.DecimalField(max_digits=10, decimal_places=2)
    turnover = models.IntegerField()
    operations = models.CharField(
        max_length=20, choices=OPERATIONS_CHOICES, default='register')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصول'

    def __str__(self):
        return self.name
