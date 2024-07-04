from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    pl = models.DecimalField(max_digits=10, decimal_places=2)
    positions = models.JSONField()  # Assuming positions is a JSON field

    def __str__(self):
        return f'{self.account_type} Account - {self.user.name}'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_type = models.CharField(max_length=50)
    time_in_force = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order {self.order_id} - {self.stock_symbol}'


class Execution(models.Model):
    execution_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField()

    def __str__(self):
        return f'Execution {self.execution_id} - {self.stock_symbol}'


class MarketData(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    stock_symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_ask_spread = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return f'Market Data {self.stock_symbol} - {self.timestamp}'


class ReferenceData(models.Model):
    stock_symbol = models.CharField(max_length=10, primary_key=True)
    exchange_code = models.CharField(max_length=10)
    industry_classification = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'Reference Data {self.stock_symbol}'
