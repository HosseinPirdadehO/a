# Generated by Django 5.0 on 2025-04-09 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images/', verbose_name='تصویر اصلی'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='product_extra_images/', verbose_name='تصویر اضافی')),
                ('alt_text', models.CharField(blank=True, max_length=255, verbose_name='متن جایگزین')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='Product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر اضافی محصول',
                'verbose_name_plural': 'تصاویر اضافی محصولات',
            },
        ),
    ]
