import alpaca_trade_api as tradeapi
import pandas as pd
from datetime import datetime, timedelta

import time

# API credentials and endpoint
API_KEY = 'PKK8UZCG2PY524JRYLHS'
API_SECRET = 'uFlyWhZdopMffswOcwJnrOhaBJSh2TVjFr41Dycc'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading for testing

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Configuration variables
account_id = 'your_account_id_here'
symbol = 'TSLA'
quantity = 100
order_type = 'market' #limit
algo_price = 190.00  # Example algorithm price
trade_action = 'buy'
stop_loss_percentage = 0.01
timeframe = 'minute'
#input divergence
#input stock_price (verify with current price) --> use the most recent one
#input algo price - 
#ticker




# Get current price of the stock
def get_current_price(symbol):
    start = (datetime.now() - timedelta(days=1)).replace(microsecond=0).isoformat() + 'Z'
    end = datetime.now().replace(microsecond=0).isoformat() + 'Z'

    barset = api.get_bars(symbol, tradeapi.TimeFrame.Minute, start=start, end=end)

    if barset:  # Check if the barset is not empty
        return barset[-1].c  # Get the latest close price from the returned Bars object
    else:
        return None  # Return None or handle it appropriately if no data is available


# Submit an order
def submit_order(symbol, qty, side, type='market', time_in_force='gtc'):
    return api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )

# Get open orders
def get_open_orders():
    return api.list_orders(status='open')

# Get account information
def get_account_info():
    return api.get_account()

# Cancel an order
def cancel_order(order_id):
    api.cancel_order(order_id)

    #close order
    #create a function for making a trading decision
    #managing the trade
    #calculate the PNL(profit and loss)
    #generate the data past 30 days - (JSON, CSV)

# Main trading logic
def main():
    holding = False
    bought_price = None

    while True:
        current_price = get_current_price(symbol)

        if current_price is None:
            print("No data available for the current time. Retrying...")
            time.sleep(60)  # Wait and retry
            continue
        
        divergence = algo_price - current_price
        
        if not holding and divergence > 0:
            order = submit_order(symbol, quantity, trade_action)
            holding = True
            bought_price = current_price
            print(f"Bought {quantity} shares at {current_price}. Order ID: {order.id}")
        
        elif holding:
            # Sell based on conditions
            if current_price <= bought_price * (1 - stop_loss_percentage) or divergence <= 0:
                order = submit_order(symbol, quantity, 'sell')
                holding = False
                print(f"Sold {quantity} shares at {current_price}. Order ID: {order.id}")
        
        time.sleep(60)  # Sleep for a minute before next check

if __name__ == '__main__':
    main()
