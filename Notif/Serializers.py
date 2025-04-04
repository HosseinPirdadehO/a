from .models import AdvertisementNotification
from .models import ContentNotification
from .models import ModalNotification
from rest_framework import serializers
from .models import NotificationSms


class NotificationSmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSms
        fields = '__all__'


class ModalNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalNotification
        fields = '__all__'


class ContentNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentNotification
        fields = '__all__'


class AdvertisementNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementNotification
        fields = '__all__'
