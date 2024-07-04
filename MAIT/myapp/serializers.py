from rest_framework import serializers
from .models import User, Account, Order, Execution, MarketData, ReferenceData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    side = serializers.CharField(write_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class ExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execution
        fields = '__all__'


class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketData
        fields = '__all__'


class ReferenceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceData
        fields = '__all__'
