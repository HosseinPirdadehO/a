from rest_framework import serializers
from Account.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'password', 'confirm_password',
            'first_name', 'last_name', 'phone_number',
            'national_id', 'role', 'city', 'province'
        ]

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "این نام کاربری قبلاً ثبت شده است.")
        return value

    def validate_phone_number(self, value):
        if CustomUser.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(
                "این شماره تماس قبلاً استفاده شده است.")
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError(
                "شماره تماس باید ۱۱ رقم و فقط عدد باشد.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"password": "رمز عبور و تکرار آن یکسان نیستند."})
        try:
            validate_password(data['password'])
        except DjangoValidationError as e:
            raise ValidationError({"password": list(e.messages)})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            national_id=validated_data.get('national_id', ''),
            role=validated_data.get('role', ''),
            city=validated_data.get('city'),
            province=validated_data.get('province'),
        )
        return user


class AdminDashboardSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_sellers = serializers.IntegerField()
    total_marketers = serializers.IntegerField()
    total_buyers = serializers.IntegerField()
    active_users = serializers.IntegerField()
    inactive_users = serializers.IntegerField()


class SellerDashboardSerializer(serializers.ModelSerializer):
    province = serializers.CharField(source='province.name', default=None)
    city = serializers.CharField(source='city.name', default=None)

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'wallet_status',
            'province',
            'city',
            'status'
        ]


class MarketerDashboardSerializer(serializers.Serializer):
    message = serializers.CharField()
    invited_users_count = serializers.IntegerField()
    city = serializers.CharField()
    wallet_status = serializers.DecimalField(max_digits=10, decimal_places=2)
