# Generated by Django 5.1.6 on 2025-04-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0005_payment_operations'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanciallySettled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, verbose_name='شماره سفارش')),
                ('purchase_type', models.CharField(max_length=50, verbose_name='نوع خرید')),
                ('product_items', models.TextField(verbose_name='اقلام کالایی')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ کل')),
                ('order_date', models.DateField(verbose_name='تاریخ سفارش')),
                ('delivery_date', models.DateField(verbose_name='تاریخ تحویل')),
                ('settlement_date', models.DateField(verbose_name=' تاریخ تصویه حساب')),
                ('settlement_info', models.TextField(verbose_name='اطلاعات تسویه')),
                ('document', models.FileField(upload_to='documents/', verbose_name='سند')),
                ('operation', models.CharField(max_length=50, verbose_name='عملیات')),
                ('product_name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('quantity', models.IntegerField(verbose_name='تعداد')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='فی')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='جمع مبلغ')),
                ('settlement_type', models.CharField(max_length=50, verbose_name='نوع تسویه')),
                ('referred_to', models.CharField(max_length=50, verbose_name='ارجاع به ')),
                ('explainer_name', models.CharField(max_length=50, verbose_name='نام توضیح کننده')),
            ],
            options={
                'verbose_name': 'مالی خریدار تسویه شده',
                'verbose_name_plural': 'مالی خریدار تسویه شده',
            },
        ),
    ]
