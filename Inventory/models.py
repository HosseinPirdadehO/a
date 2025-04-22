from django.db import models


class Inventory(models.Model):
    image = models.ImageField(
        upload_to='inventory_images/', null=True, blank=True)
    product_name = models.CharField(max_length=255)
    stock = models.IntegerField()
    unit = models.CharField(max_length=50)
    stock_alert = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacture_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    expiry_threshold = models.IntegerField(
        help_text="Days before expiry to alert", null=True, blank=True)
    sale_status = models.CharField(max_length=50, choices=[(
        'Available', 'Available'), ('Sold Out', 'Sold Out')])
    sale_range = models.CharField(max_length=255, null=True, blank=True)
    marketer_profit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    turnover = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    operations = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'موجوی'
        verbose_name_plural = ' موجوی'

    def __str__(self):
        return self.product_name
