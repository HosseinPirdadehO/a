# Generated by Django 5.1.6 on 2025-03-06 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shopper', '0002_alter_buyer_current_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]
