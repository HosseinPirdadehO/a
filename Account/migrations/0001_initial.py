# Generated by Django 5.1.6 on 2025-03-05 14:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('buyer', 'خریدار'), ('seller', 'فروشنده'), ('marketer', 'بازاریاب')], max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('national_id', models.CharField(max_length=10)),
                ('wallet_status', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('messenger', models.CharField(max_length=255)),
                ('operations', models.CharField(choices=[('created', 'ایجاد'), ('edited', 'ویرایش'), ('not_created', 'ایجاد نشده')], max_length=12)),
                ('status', models.CharField(choices=[('active', 'فعال'), ('inactive', 'غیرفعال')], max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.region')),
            ],
        ),
    ]
