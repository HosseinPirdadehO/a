# Generated by Django 5.2 on 2025-04-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام برند')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='brand_images/', verbose_name='تصویر برند')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته\u200cبندی')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
            },
        ),
    ]
