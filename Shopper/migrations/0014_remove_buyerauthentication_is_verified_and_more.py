# Generated by Django 5.1.6 on 2025-04-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopper', '0013_buyerauthentication_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyerauthentication',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='buyerauthentication',
            name='contact_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buyerauthentication',
            name='national_id',
            field=models.BooleanField(default=False),
        ),
    ]
