from .models import RequestActivation
from rest_framework import serializers
from .models import Payment, MarketerPayment, HistoryMarketerPayment, ProductPayment, FinanciallySettled


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


class FinanciallySettledSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanciallySettled
        fields = '__all__'


class RequestActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestActivation
        fields = '__all__'
