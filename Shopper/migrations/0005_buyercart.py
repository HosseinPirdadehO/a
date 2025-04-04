# Generated by Django 5.1.6 on 2025-03-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopper', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50)),
                ('purchase_type', models.CharField(max_length=50)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('settlement_type', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
