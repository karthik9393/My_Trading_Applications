
## Stock Trading Bot Using Alpaca API

This Python script (`stock_trader.py`) automates trading actions based on algorithmic price calculations. It is designed to integrate with the Alpaca trading platform using Alpaca's paper trading API, which simulates trading without financial risk.

### Features

- **Automatic Buying and Selling**: Buys or sells stocks based on calculated divergence between a predefined algorithmic price and the current market price.
- **Stop Loss Implementation**: Automatically sells stocks if the price falls below a certain threshold to limit potential losses.
- **Continuous Monitoring**: Runs in a loop, checking stock prices every minute and making trading decisions.

### Configuration Variables

- **Account ID**: Specified by the user.
- **Symbol**: Currently set to trade Apple Inc. (AAPL).
- **Quantity**: Number of shares to trade (default is 100).
- **Order Type**: Market order.
- **Algorithm Price**: Set to 250.00 as an example.
- **Trade Action**: Buy.
- **Stop Loss Percentage**: 1%.
- **Time Frame**: Minute-by-minute trading data.

### Dependencies

To run this script, you'll need Python installed on your machine along with several third-party libraries:

- `alpaca_trade_api`
- `pandas`
- `datetime`

You can install these dependencies via pip:

```bash
pip install alpaca_trade_api pandas
```

### Setup Instructions

1. **Clone or Download This Repository**
   - Clone this repo to your local machine using `git clone` or simply download the `.py` file.

2. **API Credentials**
   - Sign up for an Alpaca account at [Alpaca](https://alpaca.markets/).
   - Obtain your API key and secret, and insert them into the script.

3. **Adjust Configuration Variables**
   - Set the `account_id` and other trading parameters as needed.

### Running the Script

- **Windows Command Prompt**:
  ```bash
  python stock_trader.py
  ```

- **Mac Terminal**:
  ```bash
  python3 stock_trader.py
  ```

Ensure your command line tool is navigated to the directory containing the script before running these commands.

### Important Notes

- This script uses paper trading accounts, which means all trades are simulated and no real money is involved.
- Ensure that the trading parameters match your requirements and understand the implications of automated trading.
