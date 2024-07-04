# mytradingapp/trading/models.py

from django.db import models

class TradeOrder(models.Model):
    account_id = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField(default=100)
    order_type = models.CharField(max_length=10, default='Market')
    algo_price = models.DecimalField(max_digits=10, decimal_places=2)
    trade_action = models.CharField(max_length=4)  # 'Buy' or 'Sell'
    stop_loss_percentage = models.DecimalField(max_digits=3, decimal_places=2, default=-1.00)
    timeframe = models.CharField(max_length=50)
    executed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.trade_action} {self.quantity} of {self.symbol} at {self.algo_price}"
