from django.db import models

# فاکتور فروش کالا


class Order(models.Model):
    buyer = models.CharField(max_length=255)
    order_date = models.DateField()
    order_number = models.CharField(max_length=50, unique=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_location = models.CharField(max_length=255)
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    order_method = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_discount = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)
    shipping_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2)
    order_code = models.CharField(
        max_length=50, unique=True, null=True)

    def __str__(self):
        return f"Order #{self.order_number} - Code: {self.order_code} by {self.buyer}"
