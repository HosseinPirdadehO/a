from rest_framework import serializers
from .models import Shopper, Buyer, BuyerCart, BuyerProduct, PurchaseHistory, PurchaseHistoryProduct, BuyerAuthentication


class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class BuyerCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerCart
        fields = '__all__'


class BuyerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerProduct
        fields = '__all__'


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__'


class PurchaseHistoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistoryProduct
        fields = '__all__'


class BuyerAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerAuthentication
        fields = '__all__'
