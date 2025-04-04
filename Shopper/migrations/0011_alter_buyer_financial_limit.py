# Generated by Django 5.1.6 on 2025-04-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopper', '0010_alter_shopper_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='financial_limit',
            field=models.CharField(choices=[('cash', 'نقد'), ('check', 'چک'), ('promissory_note', 'سفته'), ('Wallet', 'کیف پول'), ('Gateway', 'درگاه'), ('Cardreader', 'کارتخوان')], max_length=15),
        ),
    ]
