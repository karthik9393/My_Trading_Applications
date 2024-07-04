from flask import Blueprint, request, jsonify
import os
import time
from .market_data_service import get_current_price
from alpaca_trade_api.rest import REST, TimeFrame

trading_data = Blueprint('trading_data', __name__)
api = REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_API_SECRET'), os.getenv('ALPACA_API_URL'))

@trading_data.route('/execute_trade', methods=['POST'])
def execute_trade():
    req_data = request.get_json()
    ticker = req_data['ticker']
    quantity = req_data.get('quantity', 100)
    order_type = req_data.get('order_type', 'limit')
    algo_price = req_data['algo_price']
    divergence = req_data['divergence']
    stop_loss_percentage = req_data['stop_loss_percentage']
    limit_price = req_data.get('limit_price', None)  # Get limit price from request

    holding = False
    bought_price = None

    current_price = get_current_price(ticker)
    if current_price is None:
        return jsonify({"error": "No data available for the current time. Retrying..."}), 503

    if not holding and divergence > 0 and order_type == "limit" and limit_price is not None:
        order = submit_order(ticker, quantity, 'buy', order_type, limit_price)
        holding = True
        bought_price = current_price
        return jsonify({"message": f"Bought {quantity} shares at {current_price}. Order ID: {order.id}"})

    elif holding:
        if current_price <= bought_price * (1 - stop_loss_percentage) or divergence <= 0:
            order = submit_order(ticker, quantity, 'sell', order_type, limit_price)
            holding = False
            return jsonify({"message": f"Sold {quantity} shares at {current_price}. Order ID: {order.id}"})

    return jsonify({"message": "Trade executed", "order_id": order.id})

def submit_order(symbol, qty, side, type='market', limit_price=None, time_in_force='gtc'):
    print(f"Submitting order {side} {qty} shares of {symbol} at limit price {limit_price}")
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        limit_price=limit_price,  # Provide limit price here
        time_in_force=time_in_force
    )
    return order
