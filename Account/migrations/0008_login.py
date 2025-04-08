# Generated by Django 5.0 on 2025-04-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='نام کاربری')),
                ('password', models.CharField(max_length=255, verbose_name='رمز عبور')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن')),
            ],
            options={
                'verbose_name': 'ورود',
                'verbose_name_plural': 'ورودها',
            },
        ),
    ]
