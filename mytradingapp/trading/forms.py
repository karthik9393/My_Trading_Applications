# mytradingapp/trading/forms.py

from django import forms
from .models import TradeOrder  # Ensure this import is correct

class TradingForm(forms.ModelForm):
    class Meta:
        model = TradeOrder
        fields = ['account_id', 'symbol', 'quantity', 'order_type', 'algo_price', 'trade_action', 'stop_loss_percentage', 'timeframe']
        widgets = {
            'order_type': forms.Select(choices=[('Market', 'Market')]),
            'trade_action': forms.Select(choices=[('Buy', 'Buy'), ('Sell', 'Sell')]),
        }
