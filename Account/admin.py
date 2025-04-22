from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'first_name', 'last_name', 'email', 'role',
        'phone_number', 'national_id', 'province', 'city',
        'wallet_status', 'status'
    )
    list_filter = ('role', 'status', 'province', 'city')
    search_fields = ('username', 'first_name', 'last_name',
                     'email', 'phone_number', 'national_id')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number', 'national_id',
                'province', 'city', 'messenger'
            )
        }),
        ('نقش و وضعیت', {
            'fields': (
                'role', 'operations', 'status', 'wallet_status'
            )
        }),
        ('دسترسی‌ها', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        ('تاریخ‌ها', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
                'first_name', 'last_name', 'email',
                'phone_number', 'national_id',
                'province', 'city', 'role', 'status', 'operations',
                'wallet_status', 'messenger'
            ),
        }),
    )
