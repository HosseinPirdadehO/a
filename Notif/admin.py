from .models import ContentNotification, AdvertisementNotification
from django.contrib import admin
from .models import NotificationSms, ModalNotification
from django.utils.html import format_html

# Register your models here.


@admin.register(NotificationSms)
class NotificationSmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'user_group',
                    'is_selected', 'action_preview')
    # فیلترگذاری براساس شهر، گروه کاربران و وضعیت انتخاب
    list_filter = ('city', 'user_group', 'is_selected')
    search_fields = ('title', 'content')  # جستجو براساس سرفصل و متن
    actions = ['mark_as_selected', 'unmark_as_selected']  # اکشن‌های سفارشی

    def action_preview(self, obj):
        if obj.action:
            return obj.action[:50]  # نمایش ۵۰ کاراکتر اول اقدام
        return "بدون اقدام"
    action_preview.short_description = 'پیش‌نمایش اقدام'

    def mark_as_selected(self, request, queryset):
        queryset.update(is_selected=True)
        self.message_user(
            request, "آیتم‌های انتخاب‌شده به حالت انتخاب شده تغییر یافتند.")
    mark_as_selected.short_description = "تغییر وضعیت به انتخاب شده"

    def unmark_as_selected(self, request, queryset):
        queryset.update(is_selected=False)
        self.message_user(
            request, "آیتم‌های انتخاب‌شده به حالت انتخاب نشده تغییر یافتند.")
    unmark_as_selected.short_description = "تغییر وضعیت به انتخاب نشده"


@admin.register(ModalNotification)
class ModalNotificationAdmin(admin.ModelAdmin):
    list_display = ('content_preview', 'province', 'city',
                    'user_group', 'image_preview', 'link')
    # فیلترگذاری براساس استان، شهر و گروه کاربران
    list_filter = ('province', 'city', 'user_group')
    # جستجو براساس متن اطلاع‌رسانی و نام فرد
    search_fields = ('content', 'individual')
    # فیلد فقط‌خواندنی برای پیش‌نمایش تصویر
    readonly_fields = ('image_preview',)

    def content_preview(self, obj):
        return obj.content[:50]  # نمایش ۵۰ کاراکتر اول متن اطلاع‌رسانی
    content_preview.short_description = 'پیش‌نمایش متن'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "بدون تصویر"
    image_preview.short_description = 'پیش‌نمایش تصویر'


@admin.register(ContentNotification)
class ContentNotificationAdmin(admin.ModelAdmin):
    list_display = ('content', 'province', 'city', 'user_group', 'link')
    list_filter = ('province', 'city', 'user_group')
    search_fields = ('content', 'individual', 'user_group')
    ordering = ('province',)


@admin.register(AdvertisementNotification)
class AdvertisementNotificationAdmin(admin.ModelAdmin):
    list_display = ('content', 'province', 'city', 'user_group', 'link')
    list_filter = ('province', 'city', 'user_group')
    search_fields = ('content', 'individual', 'user_group')
    ordering = ('province',)
