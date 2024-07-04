import os
import logging
from alpaca_trade_api.rest import REST, TimeFrame
from .models import Order, Execution

logger = logging.getLogger(__name__)

ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
ALPACA_SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
ALPACA_BASE_URL = os.getenv('ALPACA_BASE_URL')

api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, api_version='v2')

class TradingService:
    @staticmethod
    def create_order(user, stock_symbol, quantity, price, order_type, time_in_force, side):
        try:
            order = api.submit_order(
                symbol=stock_symbol,
                qty=quantity,
                side=side,
                type=order_type,
                time_in_force=time_in_force,
                limit_price=price if order_type == 'limit' else None
            )
            # Save the order to the database
            new_order = Order.objects.create(
                user=user,
                stock_symbol=stock_symbol,
                quantity=quantity,
                price=price,
                order_type=order_type,
                time_in_force=time_in_force,
                status='submitted'
            )
            new_order.save()
            return new_order
        except Exception as e:
            logger.error(f"An error occurred while creating order: {e}")
            return None

    @staticmethod
    def fetch_order_status(order_id):
        try:
            alpaca_order = api.get_order(order_id)
            return alpaca_order.status
        except Exception as e:
            logger.error(f"An error occurred while fetching order status: {e}")
            return None

    @staticmethod
    def fetch_market_data(stock_symbol, start_date, end_date):
        try:
            barset = api.get_barset(stock_symbol, TimeFrame.Day, start=start_date, end=end_date)
            return barset[stock_symbol]
        except Exception as e:
            logger.error(f"An error occurred while fetching market data: {e}")
            return None
