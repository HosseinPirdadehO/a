from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role',
                    'phone_number', 'wallet_status', 'status', 'created_at')
    list_filter = ('role', 'status', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'national_id')
    ordering = ('-created_at',)


admin.site.site_header = "مدیریت سایت"
admin.site.index_title = "خوش آمدید به پنل مدیریت"
admin.site.site_title = "عنوان مرورگر"
