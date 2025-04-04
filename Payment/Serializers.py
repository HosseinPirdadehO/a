from rest_framework import serializers
from .models import Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment


from rest_framework import serializers
from .models import Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment, BuyerPayment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class MarketerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketerPayment
        fields = '__all__'


class HistoryMarketerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryMarketerPayment
        fields = '__all__'


class ProductPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPayment
        fields = '__all__'


class BuyerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerPayment
        fields = '__all__'
