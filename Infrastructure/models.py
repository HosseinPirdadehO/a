from django.db import models

# Create your models here.

# مدل دسته‌بندی


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='نام دسته‌بندی')  # نام دسته‌بندی
    description = models.TextField(verbose_name='توضیحات')  # توضیحات دسته‌بندی

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name

# مدل برند


class Brand(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='نام برند')  # نام برند
    description = models.TextField(verbose_name='توضیحات')  # توضیحات برند
    image = models.ImageField(
        upload_to='brand_images/', verbose_name='تصویر برند')  # تصویر برند

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

    def __str__(self):
        return self.name
