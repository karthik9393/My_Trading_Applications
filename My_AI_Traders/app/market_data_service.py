from flask import Blueprint, jsonify, request
import os
from alpaca_trade_api.rest import REST, TimeFrame
import requests
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta 

api = REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_API_SECRET'), os.getenv('ALPACA_API_URL'))

market_data = Blueprint('market_data', __name__)

@market_data.route('/current_price/<ticker>', methods=['GET'])
def get_current_price(ticker):
    try:
        # Fetch the current price using the Alpaca API
        start = (datetime.now() - timedelta(minutes=10)).isoformat() + 'Z'  # small buffer to ensure data
        end = datetime.now().isoformat() + 'Z'
        barset = api.get_bars(ticker, TimeFrame.Minute, start=start, end=end)
        if barset:
            current_price = barset[-1].c  # Get the latest close price
            return jsonify({"ticker": ticker, "current_price": current_price})
        else:
            return jsonify({"error": "No data available "}), 404
    except Exception as e:
        return jsonify({"error": "Failed to fetch data", "message": str(e)}), 500


@market_data.route('/historical_data/<ticker>', methods=['GET'])
def get_historical_data(ticker):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)  # Requesting data for the last 60 days

    # Fetch historical data using yfinance
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(period='1d', interval= '15m', start=start_date, end=end_date)

    if data.empty:
        return jsonify({"error": "No historical data found for the requested ticker"}), 404

    # Save the data to a CSV file
    csv_filename = f"{ticker}_historical_data.csv"
    data.to_csv(csv_filename, index=True)

    return jsonify({"message": "Data fetched successfully", "file": csv_filename})