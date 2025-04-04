from django.db import models


# Create your models here.

class NotificationSms(models.Model):
    title = models.CharField(max_length=255)  # سرفصل اطلاع رسانی
    content = models.TextField()  # متن اطلاع رسانی
    city = models.CharField(max_length=100)  # شهر مربوطه
    user_group = models.CharField(
        max_length=255, help_text="گروه کاربران هدف")  # گروه کاربران
    is_selected = models.BooleanField(default=False)  # انتخاب شده یا خیر
    # اقدام مرتبط با اطلاع‌رسانی
    action = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'پیامک'
        verbose_name_plural = 'پیامک'

    def __str__(self):
        return self.title


class ModalNotification(models.Model):
    # تصویر مربوط به اطلاع‌رسانی
    image = models.ImageField(upload_to='modal_images/', null=True, blank=True)
    # قسمت اضافه کردن لینک
    link = models.URLField(null=True, blank=True,
                           help_text="لینک مرتبط با اطلاع‌رسانی")
    content = models.TextField()  # متن اطلاع‌رسانی
    province = models.CharField(max_length=100)  # استان
    city = models.CharField(max_length=100)  # شهر
    individual = models.CharField(
        max_length=255, null=True, blank=True, help_text="نام فرد مشخص‌شده")  # فرد مورد نظر
    user_group = models.CharField(
        max_length=255, help_text="گروه کاربران هدف")  # گروه کاربران
    # اقدامات مرتبط با اطلاع‌رسانی
    action = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'مودال'
        verbose_name_plural = 'مودال'

    def __str__(self):
        return self.content[:50]  # نمایش خلاصه‌ای از متن اطلاع‌رسانی


class ContentNotification(models.Model):
    image = models.ImageField(upload_to='modal_images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True,
                           help_text="لینک مرتبط با اطلاع‌رسانی")
    content = models.TextField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    individual = models.CharField(
        max_length=255, null=True, blank=True, help_text="نام فرد مشخص‌شده")
    user_group = models.CharField(
        max_length=255, help_text="گروه کاربران هدف")
    action = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'محتوا'
        verbose_name_plural = 'محتوا'

    def __str__(self):
        return self.content[:50]

# مدل تبلیغات


class AdvertisementNotification(models.Model):
    image = models.ImageField(upload_to='modal_images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True,
                           help_text="لینک مرتبط با اطلاع‌رسانی")
    content = models.TextField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    individual = models.CharField(
        max_length=255, null=True, blank=True, help_text="نام فرد مشخص‌شده")
    user_group = models.CharField(
        max_length=255, help_text="گروه کاربران هدف")
    action = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'تبلیغات'
        verbose_name_plural = 'تبلیغات'

    def __str__(self):
        return self.content[:50]
