from flask import Flask

def create_app():
    app = Flask(__name__)
    from .market_data_service import market_data
    app.register_blueprint(market_data)
    from .trading_service import trading_data
    app.register_blueprint(trading_data)

    return app